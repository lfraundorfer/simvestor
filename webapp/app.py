# webapp/adapter.py
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))


from flask import Flask, render_template, request, jsonify, session, send_file
from io import BytesIO
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np  # ← missing
import os

from adapter import start_game, apply_action, public_view
from state import store

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET", "dev-secret")

def _sid():
    return session.setdefault("sid", os.urandom(8).hex())

@app.get("/")
def index():
    return render_template("index.html")


@app.get("/plot.png")   # ← you missed the @
def plot_png():
    sid = _sid()
    s = store.get(sid)
    if not s:
        return ("no game", 400)

    day = min(s["day_idx"], len(s["series"]) - 1)
    end_idx = day                                # show Day 0..Day
    prices = [row.close_price for row in s["series"][: end_idx + 1]]
    x = np.arange(1, len(prices) + 1)

    fig, ax = plt.subplots()
    ax.grid(True)
    ax.plot(x, prices, marker="o")
    ax.set_title(f"Day {len(prices) - 1}")
    ax.set_xticks(x)
    ax.set_xticklabels([f"Day {i}" for i in x])

    events = s.get("events", [])
    cmap = {"BUY": "green", "SELL": "red"}
    mmap = {"BUY": "^", "SELL": "v"}

    # marker at the same day used for the decision: xi = decision_day + 1
    for ev in events:
        xi = ev["i"] + 1
        if 1 <= xi <= len(prices):
            act = ev["action"]
            ax.plot(xi, prices[xi - 1], marker=mmap.get(act, "o"),
                    color=cmap.get(act, "black"), markersize=10, linestyle="None")

    buf = BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight")
    plt.close(fig)
    buf.seek(0)
    return send_file(buf, mimetype="image/png")





@app.post("/start")
def start():
    sid = _sid()
    state = start_game(request.form.to_dict() or {})
    store[sid] = state                         # save INTERNAL state
    return render_template("play.html", **public_view(state))

@app.post("/act")
def do_act():
    sid = _sid()
    if sid not in store:
        return ("no active game, POST /start first", 400)
    action = (request.form.get("action") or "HOLD").upper()
    state = apply_action(store[sid], action)   # update INTERNAL
    store[sid] = state
    return render_template("play.html", **public_view(state))

@app.get("/state")
def state():
    sid = _sid()
    s = store.get(sid)
    return jsonify(public_view(s)) if s else jsonify({"ok": False, "message": "no game"})
