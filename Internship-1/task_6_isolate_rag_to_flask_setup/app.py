import os
import jwt
import datetime
from functools import wraps
from dotenv import load_dotenv
from flask import Flask, jsonify, request, make_response
from rag import RAG
from qdrant import Qdrant
from llm_handle.llm_models import get_llm_model

# Initialize LLM and RAG

advanced_llm = get_llm_model(
    model_provider=os.getenv('ADVANCED_LLM_PROVIDER'),
    model_version=os.getenv('ADVANCED_LLM_VERSION')
)
qdrant_client = Qdrant(advanced_llm)
rag = RAG(client=qdrant_client, llm=advanced_llm)



load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

if not app.config['SECRET_KEY']:
    raise ValueError("SECRET_KEY is not set in the environment variables.")


def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        token = token.split(" ")[1]

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            request.username = data['user']
        except:
            return jsonify({'message': 'Token is invalid!'}), 403
        return func(*args, **kwargs)
    return decorated

@app.route('/public', methods=['GET'])
def public():
    return jsonify({'message': 'Welcome to the public endpoint.'})

@app.route('/login', methods=['GET'])
def login():
    auth = request.authorization

    if auth and auth.password == 'password':
        token = jwt.encode({
            'user': auth.username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
            }, app.config['SECRET_KEY'], algorithm="HS256")

        return jsonify({'token': token})
    return make_response("Unable to verify!", 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})

@app.route('/protected', methods=['GET'])
@token_required
def protected():
    return jsonify({'message': 'JWT is verified. Welcome to the protected endpoint.'})


@app.route('/query', methods=['POST'])
@token_required

def query():
    data = request.get_json()
    if not data or 'query' not in data:
        return jsonify({'error': 'Query is required'}), 400

    try:
        user_id = request.headers.get('X-User-ID', 'default_user')
        response = rag.get_result_from_rag(data['query'], user_id)
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500



@app.route('/upload', methods=['POST'])

@token_required

def upload_document():

    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    if not file.filename:
        return jsonify({'error': 'No file selected'}), 400
    try:
        user_id = request.headers.get('X-User-ID', 'default_user')
        response = rag.save_retrievable_docs(file, user_id, filter=True)
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True)
