from flask import Flask, request, jsonify
from bardapi import Bard
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

CORS(app)

# Function to get bard's  answer 
def bard_answer(query):
    try:
        answer = Bard().get_answer(query)
        return answer['content']
    except Exception as e:
        return str(e)
    
#api
@app.route('/get_answer', methods=['GET'])
def get_answer():
    query = request.args.get('query') 

    if query is not None:
        response = bard_answer(query)
        return jsonify({'response': response})
    else:
        return jsonify({'error': 'Invalid request. Missing "query" parameter.'}), 400

if __name__ == '__main__':

    import logging
    logging.basicConfig(level=logging.INFO)
    app.run(debug=True)

