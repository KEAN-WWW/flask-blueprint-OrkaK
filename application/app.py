from flask import Flask
from application.bp.homepage.homepage import homepage

app = Flask(__name__)

# Register the 'homepage' Blueprint
app.register_blueprint(homepage)

if __name__ == '__main__':
    app.run(debug=True)
