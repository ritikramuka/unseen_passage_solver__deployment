import transformers

from transformers import pipeline

from  app import  *

def solve(question, passage):
    ups = pipeline('question-answering',model="deepset/roberta-base-squad2")
    answer = ups(question= question, context = passage )
    return answer