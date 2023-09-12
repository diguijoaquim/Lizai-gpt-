from flask import Flask, render_template, request
from flask_cors import CORS
from responde import Responder
app = Flask(__name__)
app.static_url_path = '/static'
CORS(app)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api_ghost', methods=['POST'])
def receberdados():
    print(request.data.decode('utf-8')) 
    return Responder.responder_chat(request.form['msg'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
    
