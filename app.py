from email import message
from urllib import response
from flask import Flask, render_template, request, jsonify

from chat import get_response

app = Flask(__name__)

# @app.get("/")
# # Render base html
# def  index_get():
#     return render_template("index.html")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/base")
def base():
    return render_template("base.html")

@app.post("/predict")
# route to do the prediction
def predict():
    text  = request.get_json().get("message")
    #TO DO: check if text is valid 

    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug= True)

