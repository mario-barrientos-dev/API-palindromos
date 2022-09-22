from flask import Flask
from routes.auth import routes_auth
from routes.palidromo import palindromo
from routes.welcome import welcome
from dotenv import load_dotenv
app = Flask(__name__)

app.register_blueprint(routes_auth, url_prefix="/")
app.register_blueprint(palindromo, url_prefix="/")
app.register_blueprint(welcome, url_prefix="/")

if __name__ == '__main__':
    load_dotenv()
    app.run(debug=True, port="4000")
