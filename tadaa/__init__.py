from flask import Flask
from uuid import uuid4

app = Flask(__name__)

#app.secret_key = uuid4().hex

from tadaa import config
from tadaa import routes