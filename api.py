import json

from flask import Flask, render_template, request, url_for
from articles import process_single_article
from context import get_login_token, get_types
app = Flask(__name__)

from raven import Client
client = Client(
    'https://99f7cb4fd29148f783ef5300f867570d:dabc526c069241dd852cc2b756c2cd06@app.getsentry.com/69539')


types = {}


@app.route("/knowledge_server", methods=['POST'])
def knowledge_server():
    if request.method == 'POST':
        content = request.json
        token = get_login_token()
        res = process_single_article.apply_async([content['id'], types, token])
        return str(res.task_id)
        return "X"

if __name__ == "__main__":
    token = get_login_token()
    types = get_types(token)
    app.run(port=int("8000"))
