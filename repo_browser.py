import os
import subprocess

from flask import Blueprint
from flask.ext.autoindex import AutoIndexBlueprint

from config import STORAGE_DIR

blueprint = Blueprint('repo_browser', __name__)
AutoIndexBlueprint(blueprint,STORAGE_DIR)


def init_yum_repo():
    if not os.path.isdir(STORAGE_DIR + "/repodata"):
        subprocess.call(['createrepo', '-v', STORAGE_DIR])


def update_yum_repo():
    subprocess.call(['createrepo', '-v', '--update', STORAGE_DIR])