from flask import Flask, Blueprint

import repo_browser

app = Flask(__name__)

app.register_blueprint(repo_browser.blueprint, url_prefix="/repo")

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()