# DocBot - AI Document Query Chatbot
## Table of Content

- Overview
- Technical Aspect
- Installation
- Troubleshooting
- Directory Tree
- Bug / Feature Request
- Technologies Used

## Overview
DocBot is an AI-powered chatbot built on the foundation of OpenAI's GPT-3.5 and the Streamlit framework. The bot can retrieve answers from documents provided in its directory, allowing users to ask questions about the document's content and get precise answers. This is achieved by indexing the document content into a vector database and leveraging the language model's capabilities for answering the questions.



## Technical Aspect
The DocBot project revolves around these primary functionalities:

1. Loading and processing various document types, including PDF, DOCX, and TXT.
2. Indexing document content for efficient retrieval.
3. Answering user queries by searching through these documents.

Both tasks are executed using OpenAI's GPT-3.5 language model and enhanced with the Streamlit framework for an interactive web interface.

## Installation

The installation steps are different for different OS.

### Linux:

```bash
python3.8 --version
apt install python3.8-venv
python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
export OPENAI_API_KEY=<your secret key>
streamlit run chatbot.py
```

### Windows:

```bash
python3.8 -m venv myenv
myenv\Scripts\activate
pip install -r requirements.txt
export OPENAI_API_KEY=<your secret key>
streamlit run chatbot.py
```

### Mac:

```bash
python3.8 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
export OPENAI_API_KEY=<your secret key>
streamlit run chatbot.py
```

Remember to replace `<your secret key>` with your actual OpenAI API Key.


## Troubleshooting

If you encounter errors while installing the dependencies from `requirements.txt`, try installing the packages individually using the following commands:

```bash
pip install openai
pip install streamlit
pip install streamlit-chat
pip install chromadb==0.3.29
pip install pypdf
pip install langchain
pip install tiktoken
```

Then, export your OpenAI API Key and run the chatbot:
```bash
export OPENAI_API_KEY=<your secret key>
streamlit run chatbot.py
```
Remember to replace `<your secret key>` with your actual OpenAI API Key.


## Directory Tree
```
├── images
│   ├── openai.png
│   ├── streamlit.jpg
├── docs
│   ├── 1706.03762.pdf
├── .gitignore
├── chatbot.py
├── requirements.txt
└── README.md
```

## Bug / Feature Request
If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/nehalvaghasiya/DocBot/issues/new) by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/nehalvaghasiya/DocBot/issues/new). Please include sample queries and their corresponding results.

## Technologies Used

<img src="images/openai.png" width="125"/><img src="images/streamlit.jpg" width="210"/> 
