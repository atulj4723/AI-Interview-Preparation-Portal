from flask import Flask
from routes.auth import auth_bp
from flask_cors import CORS
port = 3000 
app = Flask(__name__)
CORS(app)
app.register_blueprint(auth_bp)
@app.route('/')
def hello_world():
    return 'Hello, World!'
if __name__ == '__main__':
    # app.run(debug="true")
    app.run(port=3000)