from flask import Flask

app = Flask(__name__)

@app.route('/inicio')
def home():
    return ()

app.run()