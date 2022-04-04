from flask import Flask
app = Flask(__name__)
@app.route('/')

def hello_world():
    return 'Welcome to SCA Cloud School Application, This is my first asssesment'
if __name__=="__main__":
    app.run(debug=True)
