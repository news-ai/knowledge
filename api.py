from flask import Flask, render_template, request, url_for
app = Flask(__name__)


@app.route("/knowledge_server", methods=['POST'])
def knowledge_server():
    if request.method == 'POST':
        article_id = request.form['id']
        article_url = request.form['url']
        return "Hello World!"

if __name__ == "__main__":
    app.run(port=int("8000"))
