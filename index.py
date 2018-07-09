from flask import Flask, request
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jepg', 'gif'])

# For a given file, return whether it's a allowed type or not


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/register', methods=['POST'])
def register():
    print request.headers
    print request.form
    print request.form['name']
    print request.form.get('name')
    print request.form.getlist('name')
    print request.form.get('nickname', default='little apple')
    return 'welcome'


@app.route('/api/post', methods=['POST'])
def post():
    getForm = request.get_json('token')
    print getForm['token']
    return 'succeed'


@app.route('/upload', methods=['POST'])
def upload():
        upload_file = request.files['image01']
        if upload_file and allowed_file(upload_file.filename):
            filename = secure_filename(upload_file.filename)
            upload_file.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], filename))
            return 'hello, ' + request.form.get('name', 'little apple') + '. success'
        else:
            return 'hello, ' + request.form.get('name', 'little apple') + '. failed'


if __name__ == '__main__':
    app.run(debug=True)