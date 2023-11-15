#!/usr/bin/env python3
"""
Her we initialize a flask app
"""
from flask import Flask, jsonify, request, abort, redirect

from auth import Auth


app = Flask(__name__)

app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """GET the jsonify return
    """
    return jsonify({"message": "Bievenue"})



if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")