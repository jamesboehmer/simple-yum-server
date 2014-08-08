import os

from flask import Flask, request, abort
from werkzeug.utils import secure_filename

import repo_browser
import helpers
import config

app = Flask(__name__)

app.register_blueprint(repo_browser.blueprint, url_prefix="/repo")

@app.route("/packages", methods=['POST'])
def upload_packages():
    file = request.files['file']
    if file and helpers.allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(config.STORAGE_DIR, filename))
        return "Ok"
    abort(404)

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()