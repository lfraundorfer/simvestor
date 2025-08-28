# webapp/app.py
from flask import Flask, render_template, request, jsonify
from adapter import run_preview

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.post("/api/simulate")
def api_simulate():
    payload = request.get_json(silent=True) or request.form.to_dict()
    return jsonify(run_preview(payload))
