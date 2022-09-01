from app import app
from app.views.file import Views

@app.route('/', methods=['GET'])
def index():
    return Views.index()

@app.route('/', methods=['POST'])
def upload_file():
        return Views.upload_file()

@app.route('/img/<filename>')
def show_image(filename):
        return Views.show_image(filename)


if __name__ == "__main__":
    app.run()