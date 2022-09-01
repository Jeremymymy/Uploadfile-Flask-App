from flask import Flask
import os

SRC_PATH = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER_DIR = os.path.join(SRC_PATH, 'static\\uploads')

app = Flask(__name__, template_folder='templates')
app.secret_key =  b'_5#y2L"F4Q8z\n\xec]/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER_DIR