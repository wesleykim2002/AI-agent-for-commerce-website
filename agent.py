from transformers import pipeline
import clip
import torch
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class Agent:
    def __init__(self):
        # Initialize Q&A pipeline
        self.qa_pipeline = pipeline('question-answering', model='distilbert-base-uncased-distilled-squad')
        
        # Initialize CLIP for product recommendations
        self.clip_model, self.clip_preprocess = clip.load('ViT-B/32', device='cpu')
        
        # Context for Q&A
        self.context = """
        Our commerce website sells clothing, electronics, and home goods
        Policies:
        - return policy allows returns within 30 days with a receipt
        - shipping is free for orders over $50
        """

    def answer_question(self, question):
        result = self.qa_pipeline({'question': question, 'context': self.context})
        return result['answer']

    def recommend_products(self, query, products):
        query_tokens = clip.tokenize([query]).to('cpu')
        with torch.no_grad():
            query_embedding = self.clip_model.encode_text(query_tokens).numpy()
        product_scores = []
        for product in products:
            desc_tokens = clip.tokenize([product.description]).to('cpu')
            with torch.no_grad():
                desc_embedding = self.clip_model.encode_text(desc_tokens).numpy()
            score = cosine_similarity(query_embedding, desc_embedding)[0][0]
            product_scores.append((product, score))
        product_scores.sort(key=lambda x: x[1], reverse=True)
        return [p[0] for p in product_scores[:3]]