from flask import Blueprint
from flask.ext.autoindex import AutoIndexBlueprint

blueprint = Blueprint('repo_browser', __name__)
AutoIndexBlueprint(blueprint,'/tmp/storage')
