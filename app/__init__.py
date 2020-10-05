from flask import Flask


webhook_app = Flask(__name__)

from app import routes  # noqa
