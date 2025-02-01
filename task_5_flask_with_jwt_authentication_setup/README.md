# Task: Flask Project Setup with JWT Authentication

A simple Flask API with JWT-based authentication project setup. It includes endpoints for public access, user login, and a protected resource that is accessible only with a valid JWT token.

## Features
- **JWT Authentication**: Implements secure access to routes using JSON Web Tokens.
- **Login**: Basic authentication to issue JWT tokens.
- **Protected Endpoint**: Ensures only authenticated users can access certain resources.
- **Environment Configuration**: Securely manage sensitive keys using a `.env` file.
- **Testing with REST Client**: Includes a `test.rest` file for easy API testing.

## Endpoints

1. **Public Endpoint**
   - Accessible to everyone without authentication.
   - **Request**: `GET /public`
   - **Response**: `{ "message": "Welcome to the public endpoint." }`

2. **Login Endpoint**
   - Requires basic authentication.
   - Generates a JWT token valid for 30 minutes.
   - **Request**: `GET /login`
     - Authorization Header: `Basic <Base64Encoded(username:password)>`
   - **Response**: `{ "token": "<JWT Token>" }`

3. **Protected Endpoint**
   - Accessible only with a valid JWT token.
   - **Request**: `GET /protected`
     - Header: `Authorization: Bearer <JWT Token>`
   - **Response**: `{ "message": "JWT is verified. Welcome to the protected endpoint." }`

## Installation

1. Clone the repository and navigate to the project directory.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Environment Setup

1. Create a `.env` file in the project root.
2. Add the `SECRET_KEY` variable:
   ```env
   SECRET_KEY=<your_secret_key>
   ```

## Running the Application

1. Start the Flask server:
   ```bash
   python app.py
   ```
2. The application will run on `http://127.0.0.1:5000`.

## Testing

Use the included `test.rest` file with a REST client (e.g., VS Code REST Client extension):

1. Test the public route.
2. Authenticate using `GET /login` with username and password (`password`).
3. Use the JWT token from the login response to test the protected route.

## Tools and Libraries

- **Flask**: Web framework for building APIs.
- **PyJWT**: For encoding and decoding JWT tokens.
- **python-dotenv**: Manage environment variables.
