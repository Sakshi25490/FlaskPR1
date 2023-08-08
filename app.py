from flask import Flask, jsonify,request,render_template
import json

app=Flask(__name__)


@app.route('/')
def welcome():
    return "Welcome to  the Flask"

@app.route('/cal',methods=["GET"])
def math_Operator():
    operation=request.json["operation"]
    number1=request.json["number1"]
    number2=request.json["number2"]

    if operation=='add':
        result = int(number1)+int(number2)
    elif operation=='multiplication':
        result = int(number1)*int(number2)
    elif operation=='division':
        result = int(number1)/int(number2)
    else:
        result=int(number1)-int(number2)
    #return jsonify(result)
    return "This is the operation {} and the result is {}".format(operation,result)



print(__name__)

if __name__=='__main__':
    app.run(debug=True)