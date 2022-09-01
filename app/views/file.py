from flask import render_template, request, url_for, redirect, flash
#from werkzeug.utils import secure_filename
from app import UPLOAD_FOLDER_DIR, SRC_PATH
import os

filenames = []

def allowed_file(filename):
    return filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))

class Views:
    def index():
        filenames = os.listdir(UPLOAD_FOLDER_DIR)
        return render_template('index.html', filenames=filenames)

    def upload_file():
        if 'filename' not in request.files:
            flash('沒有上傳檔案')
            return redirect(url_for('index'))

        file = request.files['filename']
        if file.filename == '':
            flash('請選擇要上傳的影像')
            return redirect(url_for('index'))

        if file and allowed_file(file.filename):
            #secure_name = secure_filename(file.filename)   #secure_filename()會把中文檔名吃掉
            secure_name = file.filename.strip('../').strip('./').strip('/')
            ord_files = os.listdir(UPLOAD_FOLDER_DIR)
            number = len(ord_files) + 1
            secure_name = 'Img_{}_'.format(str(number)) + secure_name
            file.save(os.path.join(UPLOAD_FOLDER_DIR, secure_name))
            filenames.append(secure_name)
            flash('影像上傳成功!')
            return render_template('index.html', filenames=filenames)

        else:
            flash('僅允許上傳png, jpg, jpeg和gif影像檔')
            return redirect(url_for('index'))

    def show_image(filename):
        return redirect(url_for('static', filename='uploads/' + filename))