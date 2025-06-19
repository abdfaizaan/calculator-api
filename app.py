from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/')
def home():
    return "Welcome to the Calculator API! Visit /apidocs for Swagger UI."

@app.route('/add', methods=['GET'])
def add():
    """
    Add two numbers
    ---
    parameters:
      - name: a
        in: query
        type: number
        required: true
        description: First number
      - name: b
        in: query
        type: number
        required: true
        description: Second number
    responses:
      200:
        description: Result of addition
        schema:
          type: number
    """
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    return jsonify(a + b)

@app.route('/sub', methods=['GET'])
def subtract():
    """
    Subtract two numbers
    ---
    parameters:
      - name: a
        in: query
        type: number
        required: true
        description: Minuend
      - name: b
        in: query
        type: number
        required: true
        description: Subtrahend
    responses:
      200:
        description: Result of subtraction
        schema:
          type: number
    """
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    return jsonify(a - b)

@app.route('/mul', methods=['GET'])
def multiply():
    """
    Multiply two numbers
    ---
    parameters:
      - name: a
        in: query
        type: number
        required: true
        description: First factor
      - name: b
        in: query
        type: number
        required: true
        description: Second factor
    responses:
      200:
        description: Result of multiplication
        schema:
          type: number
    """
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    return jsonify(a * b)

@app.route('/div', methods=['GET'])
def divide():
    """
    Divide two numbers
    ---
    parameters:
      - name: a
        in: query
        type: number
        required: true
        description: Dividend
      - name: b
        in: query
        type: number
        required: true
        description: Divisor
    responses:
      200:
        description: Result of division
        schema:
          type: number
      400:
        description: Division by zero error
    """
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    if b == 0:
        return "Division by zero is not allowed", 400
    return jsonify(a / b)

if __name__ == '__main__':
    app.run(debug=True)
