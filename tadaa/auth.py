from flask_login import LoginManager, UserMixin
import os

# Load .env file
from dotenv import load_dotenv
load_dotenv()

from tadaa import app

login_manager = LoginManager()
login_manager.init_app(app)

# Get environment variables
USER_ID  = os.environ.get('TADAA_USER_ID')
USERNAME = os.environ.get('TADAA_USERNAME')
PASSWORD = os.environ.get('TADAA_PASSWORD')

# MARK: Authentication

class User(UserMixin):
    def __init__(self):
        self.id = USER_ID
        self.name = USERNAME
        self.password = PASSWORD

lp_user = User()

@login_manager.user_loader
def load_user(user_id):
    if user_id == USER_ID:
        return lp_user
    return None