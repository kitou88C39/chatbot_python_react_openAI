from flask import Flask

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():    
    return {'answer': ['Hey World', 'My name is', 'Almanmoun']}
