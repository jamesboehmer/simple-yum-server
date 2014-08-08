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
        repo_browser.update_yum_repo()
        return "Ok"
    abort(404)

def main():
    repo_browser.init_yum_repo()
    app.run(host="0.0.0.0", port="5000")

if __name__ == "__main__":
    main()