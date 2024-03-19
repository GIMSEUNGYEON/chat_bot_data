from flask import Flask,redirect,jsonify
from flask.globals import request
from flask.templating import render_template
from chatbot2.chatbot_test import MyModel


app = Flask(__name__)
mm = MyModel()

@app.route('/')
def index():
    output = mm.predict("감기 걸린 것 같아")
    print("output",output)
    return output
    


if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    