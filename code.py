import web
from flask import Flask
import sentry_sdk

sentry_sdk.init(release="gawctf@v1")

from web.template import ALLOWED_AST_NODES
ALLOWED_AST_NODES.append('Constant')

app = Flask(__name__)

@app.route("/")
def code():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
