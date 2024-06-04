#!/usr/bin/env python3
"""
Route module for the API
"""
import os
from os import getenv
from typing import Tuple

from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)

from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None

if getenv("AUTH_TYPE") == "auth":
    auth = Auth()
elif getenv("AUTH_TYPE") == "basic_auth":
    auth = BasicAuth()


@app.errorhandler(404)
def not_found(error) -> tuple:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error: Exception) -> Tuple[jsonify, int]:
    """Error handler for unauthorized requests.

    Args:
        error (Exception): The error raised.

    Returns:
        Tuple[jsonify, int]: JSON response with the error message and a 401
        status code.
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error: Exception) -> Tuple[jsonify, int]:
    """Error handler for unauthorized requests.

    Args:
        error (Exception): The error raised.

    Returns:
        Tuple[jsonify, int]: JSON response with the error message and a 401
        status code.
    """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_request():
    """
    Handle the request by checking for authentication and authorization.
    """
    authorized_list = ['/api/v1/status/',
                       '/api/v1/unauthorized/',
                       '/api/v1/forbidden/']

    if auth and auth.require_auth(request.path, authorized_list):
        # If auth.authorization_header(request) returns None, raise the error
        # 401 - you must use abort
        if not auth.authorization_header(request):
            abort(401)
        # If auth.current_user(request) returns None, raise the error 403 - you
        # must use abort
        if not auth.current_user(request):
            abort(403)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port, debug=True)
