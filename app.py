from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
df = pd.read_csv("Top20_Tags.csv")
CORS(app)

@app.route('/')
def home():
    return "✅ StackOverflow Data Analyzer is running! Go to /data to see the data."

@app.route("/data")
def get():
    data = df.to_dict(orient="records")
    return jsonify(data)

if __name__=='__main__':
    app.run(debug=True)
