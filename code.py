import web
from flask import Flask
import sentry_sdk

sentry_sdk.init(release="gawCTF@v1")

from web.template import ALLOWED_AST_NODES
ALLOWED_AST_NODES.append('Constant')

app = Flask(__name__)

@app.route("/")
def code():
    sum = 1 / 0
    return "Hello World!"

if __name__ == "__main__":
    app.run()
