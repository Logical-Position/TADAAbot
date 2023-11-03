import os
from tadaa import app


app.config['DATA_DIR'] = os.path.join(app.root_path, 'data')
app.config['AUDITS_DIR'] = os.path.join(app.instance_path, 'audits')

os.makedirs(app.config['AUDITS_DIR'], exist_ok=True)

app.config['MAX_FILE_SIZE'] = 1024 * 1024 * 4 # 4mb
app.config['ALLOWED_FILES'] = ['.csv', '.jpg', '.png', '.gif']