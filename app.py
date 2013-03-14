from flask import Flask, request, render_template
from flaskext.babel import Babel

from settings import DEBUG, PORT
from utils import get_statuses

DEFAULT_LOCALE = "tr"

app = Flask(__name__)
app.jinja_env.add_extension("jinja2htmlcompress.HTMLCompress")
babel = Babel(app)


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(("tr", "en"),
                                               default=DEFAULT_LOCALE)


@app.route("/")
def index():
    return render_template("index.html", statuses=get_statuses(),
                           locale=get_locale())

if __name__ == "__main__":
    import sys

    try:
        port = int(sys.argv[1])
    except (IndexError, ValueError):
        port = PORT
    app.run(port=port, debug=DEBUG)
