import os
import jwt
import datetime
from functools import wraps
from dotenv import load_dotenv
from flask import Flask, jsonify, request, make_response


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


if __name__ == '__main__':
    app.run(debug=True)
