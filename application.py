from flask import Flask
app = Flask(__name__)

@app.route("/")
def lottery():
    luckyno=7
    number=int(input("Please type a number"))
    if luckyno==number:
        return "YOU ARE RIGHT!"
    else:
        return "WRONG!"
