  GNU nano 6.2                         app.py                                   
from flask import Flask 
app = Flask(__name__)
@app.route('/')
def home():
    return 'Hello,Devops!'
if __name__ == '__main__':
    app.run(depug=True)

