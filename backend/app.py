from flask import Flask
from routes.auth import auth_bp
app = Flask(__name__)
app.register_blueprint(auth_bp)
@app.route('/')
def hello_world():
    return 'Hello, World!'
if __name__ == '__main__':
    app.run(debug="true")