from flask import redirect, render_template, Flask, request, url_for, send_file
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


if __name__=="__main__":
    app.run(
        debug=True,
        use_reloader=True,
        use_debugger=True,
        port=5000,
        host='0.0.0.0',
        use_evalex=True,
        threaded=True,
        passthrough_errors=False
        )