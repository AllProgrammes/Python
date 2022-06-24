from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/armstrong/<int:number>")
def check_armstrong(number):
    sum = 0
    copy_number = number
    order = len(str(copy_number))
    while number != 0:
        digit = number % 10
        sum += pow(digit, order)
        number = number // 10
    number = int(number)
    if sum == copy_number:  # quick check
        result={
            "Number":copy_number,
            "Is Armstrong?":True,
            "Server Address":"696.969.6969"
        }
    else:
        result={
            "Number":copy_number,
            "Is Armstrong?":False,
            "Server Address":"696.969.6969"
        }
        
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
