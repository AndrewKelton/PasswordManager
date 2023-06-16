from gen import main
from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/result", methods=['POST', 'GET'])
def result():
    while True:
        password = main()

        return render_template("index.html",password = password)

if __name__=='__main__':
    app.run(debug=True,port=5001)
