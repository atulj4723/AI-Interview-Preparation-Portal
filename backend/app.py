from flask import Flask
from routes.auth import auth_bp
from routes.profile import profile_bp
from routes.interview import interview_bp
from routes.ai import ai_bp
from routes.conversation import con_bp
from flask_cors import CORS
app = Flask(__name__)
CORS(app, supports_credentials=True)
app.register_blueprint(auth_bp)
app.register_blueprint(profile_bp)
app.register_blueprint(interview_bp)
app.register_blueprint(ai_bp)
app.register_blueprint(con_bp)
@app.route('/')
def hello_world():
    return 'Hello, World!'
if __name__ == '__main__':
    app.run(debug="true")
