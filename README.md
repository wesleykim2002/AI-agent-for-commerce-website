# AI Agent for Commerce Website

This repository contains code for an AI-powered backend agent that supports:
- General Q&A (i.e., “What’s the return policy?”)
- Text-based product recommendation (i.e., “show me stylish shoes”)


## Features

- **Question Answering** – Extracts responses from static policy context using DistilBERT.
- **Text Recommendations** – Uses OpenAI CLIP to match user queries with product descriptions.


## Tech Stack

- **Backend**: Flask (REST API)
- **AI**: Transformers (`distilbert-base-uncased-distilled-squad`) + OpenAI CLIP (`ViT-B/32`)
- **Database**: SQLite (via SQLAlchemy)
- **Others**: Torch, Scikit-Learn

The tech stack was chosen as they were deemed the most efficient for the use case
- Flask has the least amount of setup unlike other frameworks like Django
- Hugging Face's transformers library has models like DistilBERT which is pre-trained for answering questions from context blocks
- OpenAI CLIP is able to match queries with products. Additionally, it could also be used to match images with products if the feature were to be implemented.


## Installation

First, clone the repository (or download the codebase)

Then proceed with the following commands:

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# initialize database
python init_db.py

# start app
python app.py
```

## Testing

### QnA ###
Endpoint: `http://localhost:3000/api/qa`

```
> curl -X POST -H "Content-Type: application/json" -d '{"question":"What is the return policy?"}' http://localhost:3000/api/qa
> {"answer":"allows returns within 30 days with a receipt"}
```

### Recommendations ###
Endpoint: `http://localhost:3000/api/recommend`

```
> curl -X POST -H "Content-Type: application/json" -d '{"query":"lifestyle shoes"}' http://localhost:3000/api/recommend   
> {"products":[{"description":"Lifestyle shoes for men","id":1,"name":"Shoes","price":149.99},{"description":"Lifestyle shoes for men","id":4,"name":"Shoes","price":149.99},{"description":"Smart TV","id":3,"name":"TV","price":1299.99}]}

```