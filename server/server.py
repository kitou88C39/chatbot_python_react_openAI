from flask import Flask
from flask_cors import cross_origin

app = Flask(__name__)

@app.route('/ask')
@cross_origin()
def ask():    
    return {'answer': ['Hey World', 'My name is', 'Almanmoun']}

app.run()