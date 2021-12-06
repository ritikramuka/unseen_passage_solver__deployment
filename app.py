from typing import Tuple
from flask import Flask , render_template, request
from flask.signals import Namespace
import transformers

from transformers import pipeline


from model import *

app = Flask(__name__)

@app.route('/')
def hello_world():
   return render_template('index.html')



@app.route('/',methods = ['POST'] )
def getPasse():
    if request.method == "POST":
        passage = request.form["unseen_passage"]
        question = request.form["ques_input"]

    ans =  solve(question, passage)
    return render_template('index.html',passage=passage, question=question,  answer=ans['answer'])

if __name__ == '__main__':
   app.run( debug=True , port =8000)
