import uuid
import os
import streamlit as st
from langchain.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.text_splitter import CharacterTextSplitter
from streamlit_chat import message

class DocBot:
    
    def __init__(self) -> None:
        self.initialize_session_state()
        self.session_state = st.session_state
        self.documents = self._load_documents()
        self.pdf_qa = self._initialize_qa_chain()

    def initialize_session_state(self) -> None:
        """Initialize session state variables."""
        if 'chat_history' not in st.session_state:
            st.session_state['chat_history'] = []
        if 'greeting_displayed' not in st.session_state:
            st.session_state['greeting_displayed'] = False

    def _load_documents(self):
        documents = []
        available_files = []
        for file in os.listdir("docs"):
            available_files.append(file)
            if file.endswith(".pdf"):
                pdf_path = "./docs/" + file
                loader = PyPDFLoader(pdf_path)
                documents.extend(loader.load())
            elif file.endswith('.docx') or file.endswith('.doc'):
                doc_path = "./docs/" + file
                loader = Docx2txtLoader(doc_path)
                documents.extend(loader.load())
            elif file.endswith('.txt'):
                text_path = "./docs/" + file
                loader = TextLoader(text_path)
                documents.extend(loader.load())

        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=10)
        return text_splitter.split_documents(documents), available_files

    def _initialize_qa_chain(self):
        split_documents, _ = self.documents
        vectordb = Chroma.from_documents(split_documents, embedding=OpenAIEmbeddings(), persist_directory="./data")
        vectordb.persist()

        pdf_qa = ConversationalRetrievalChain.from_llm(
            ChatOpenAI(temperature=0.7, model_name='gpt-3.5-turbo'),
            retriever=vectordb.as_retriever(search_kwargs={'k': 6}),
            return_source_documents=True,
            verbose=False
        )
        return pdf_qa

    def display_past_interactions(self) -> None:
        """Display previous questions and their corresponding answers."""
        for query, answer, query_key, answer_key in self.session_state['chat_history']:
            message(query, is_user=True, key=query_key)
            message(answer, key=answer_key)

    def get_query_and_display_answer(self) -> None:
        """Get the query from the user, process it, and display the answer."""
        query = st.text_input("Your query:", key="input_query")

        if query and (not 'last_query' in self.session_state or query != self.session_state['last_query']):
            self.session_state['last_query'] = query
            result = self.pdf_qa({
                "question": query,
                "chat_history": [item[:2] for item in self.session_state['chat_history']]
            })

            if result:
                query_key = self._generate_uuid()
                answer_key = self._generate_uuid()
                self.session_state['chat_history'].append((query, result["answer"], query_key, answer_key))
                
                # Displaying the new interaction immediately
                message(query, is_user=True, key=query_key)
                message(result["answer"], key=answer_key)
                st.experimental_rerun()

    def execute_bot(self) -> None:
        """Main function to execute the chatbot."""
        if not self.session_state['greeting_displayed']:
            message("Welcome to the DocBot. You can ask questions from the following files:", key=self._generate_uuid())
            for file in self.documents[1]:  # using the available_files from the tuple returned by _load_documents
                st.write(f"- {file}")
            self.session_state['greeting_displayed'] = True

        self.display_past_interactions()  # Display previous messages
        self.get_query_and_display_answer()  # Get current input and display its response


    @staticmethod
    def _generate_uuid() -> str:
        """Generate a unique identifier."""
        return str(uuid.uuid4())

def create_bot() -> None:
    """Create and execute the DocBot."""
    bot = DocBot()
    bot.execute_bot()

st.title("DocBot - AI Document Query Chatbot")
create_bot()
