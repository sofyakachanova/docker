from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
return '<h1 style="color: #003f8c">Hello Docker world! </h1>'
