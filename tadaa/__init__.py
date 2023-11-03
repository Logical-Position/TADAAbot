from flask import Flask

app = Flask(__name__)

from tadaa import config
from tadaa import routes