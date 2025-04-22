from flask import Flask, request, jsonify
from agent import Agent
from models import db, Product

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
agent = Agent()

@app.route('/api/qa', methods=['POST'])
def qa():
    data = request.get_json()
    question = data.get('question')
    if not question:
        return jsonify({'error': 'Question is required'}), 400
    answer = agent.answer_question(question)
    return jsonify({'answer': answer})

@app.route('/api/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    query = data.get('query')
    if not query:
        return jsonify({'error': 'Query is required'}), 400
    products = agent.recommend_products(query, Product.query.all())
    return jsonify({'products': [p.to_dict() for p in products]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)