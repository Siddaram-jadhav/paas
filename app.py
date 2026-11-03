
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    current_datetime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    return f"""
    <h1>Welcome to My Application!</h1>
    <h2>Current Date and Time: {current_datetime}</h2>
    """

if __name__ == "__main__":
    app.run(debug=True)
