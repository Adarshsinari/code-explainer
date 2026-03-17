# Code Explainer API

This project is a FastAPI-based backend that uses an LLM (LangChain + Claude/OpenAI)
to explain code snippets and return structured output using Pydantic. Here we use prompt template to feth the desired results and also we are chaining structured model so that we recieve data in expected structure. 

## Setup Instructions

### 1. Clone repo

### 2. Run command 
````bash
python -m venv venv
venv\Scripts\activate
````

### 3. Install dependencies
````bash
pip install -r requirements.txt
````

### 4. Create .env file in root folder. (refer to .env.sample file)

### 5. Run server
````bash
uvicorn main:app --reload
````


