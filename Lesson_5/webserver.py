from flask import Flask, request, render_template, redirect, escape

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    result = ''
    if request.method == "POST" and "firstNumber" in request.form and "secondNumber" in request.form and "operation" in request.form:
        firstNumber = float(request.form.get('firstNumber'))
        secondNumber = float(request.form.get('secondNumber'))
        operation = str(request.form.get('operation'))
        if operation == "+":
            result = firstNumber + secondNumber
        if operation == "-":
            result = firstNumber - secondNumber
        if operation == "*":
            result = firstNumber * secondNumber
        if operation == "/":
            result = firstNumber / secondNumber
    return render_template("index.html", result=result)


app.run(host="0.0.0.0", port=8081)
