import os
from tadaa import app

#ProxyFix Middleware for Nginx
from werkzeug.middleware.proxy_fix import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1, x_prefix=1)

app.config['DATA_DIR'] = os.path.join(app.root_path, 'data')
app.config['AUDITS_DIR'] = os.path.join(app.instance_path, 'audits')

os.makedirs(app.config['AUDITS_DIR'], exist_ok=True)

app.config['MAX_FILE_SIZE'] = 1024 * 1024 * 4 # 4mb
app.config['ALLOWED_FILES'] = ['.csv', '.jpg', '.png', '.gif']