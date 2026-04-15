from flask import Flask
import os

app = Flask(__name__)

def multiply(a, b):
    return a * b

@app.route('/')
def home():
    result = multiply(143,1)
    return f"<h1>MLOps Pipeline Success!</h1><p>The multiplication of 2 and 3 is: {result}</p>"

if __name__ == "__main__":
    # Render provides a PORT environment variable
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)