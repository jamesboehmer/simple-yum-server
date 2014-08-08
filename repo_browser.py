from flask import Blueprint
from flask.ext.autoindex import AutoIndexBlueprint

from config import STORAGE_DIR

blueprint = Blueprint('repo_browser', __name__)
AutoIndexBlueprint(blueprint,STORAGE_DIR)
