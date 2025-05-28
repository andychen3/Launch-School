from flask import Flask, render_template, send_from_directory, redirect, url_for, flash, request, session
from markdown import markdown
from functools import wraps
import os
import yaml
import bcrypt

app = Flask(__name__)
app.secret_key="secret"

def valid_credentials(username, password):
    credentials = load_user_credentials()

    if username in credentials:
        stored_password = credentials[username].encode('utf-8')
        return bcrypt.checkpw(password.encode('utf-8'), stored_password)
    else:
        return False

def load_user_credentials():
    filename = 'users.yml'
    root_dir = os.path.dirname(__file__)

    credentials_path = os.path.join(root_dir, "cms", filename)

    with open(credentials_path, 'r') as file:
        return yaml.safe_load(file)

def required_sign_in(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not user_signed_in():
            flash("You must be signed in to do that")
            return redirect(url_for("show_signin_form"))
        return f(*args, **kwargs)
    return decorated_function

def user_signed_in():
    return 'username' in session


def get_data_path():
    if app.config["TESTING"]:
        return os.path.join(os.path.dirname(__file__), "tests", "data")
    else:
        return os.path.join(os.path.dirname(__file__), "cms", "data")

@app.route("/")
def index():
    data_dir = get_data_path()
    files = [os.path.basename(path) for path in os.listdir(data_dir)]
    return render_template("index.html", files=files)


@app.route("/users/signin")
def show_signin_form():
    return render_template("sign_in.html")


@app.route("/users/signin", methods=["POST"])
def signin():
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "").strip()


    if valid_credentials(username, password):
        session["username"] = username
        flash("Welcome!")
        return redirect(url_for("index"))
    else:
        flash("Invalid credentials.")
        return render_template('sign_in.html'), 422

@app.route("/users/signout", methods=["POST"])
def signout():
    session.pop('username', None)
    flash("You have been signed out.")
    return redirect(url_for('index'))

@app.route("/<filename>")
def file_content(filename):
    data_dir = get_data_path()
    file_path = os.path.join(data_dir, filename)
    
    if os.path.isfile(file_path):
        if filename.endswith(".md"):
            with open(file_path, "r") as file:
                content = file.read()
            return render_template('markdown.html', content=markdown(content))
        else:
            return send_from_directory(data_dir, filename)
    else:
        flash(f"{filename} does not exist.")
        return redirect(url_for("index"))


@app.route("/<filename>/edit")
@required_sign_in
def edit_file(filename):
    data_dir = get_data_path()
    file_path = os.path.join(data_dir, filename)

    if os.path.isfile(file_path):
        with open(file_path, "r") as file:
            content = file.read()
        return render_template('edit.html', filename=filename, content=content)
    else:
        flash(f"{filename} does not exist.")
    return redirect(url_for('index'))


@app.route("/<filename>", methods=["POST"])
@required_sign_in
def save_file(filename):
    data_dir = get_data_path()
    file_path = os.path.join(data_dir, filename)

    content = request.form['content']

    with open(file_path, "w") as file:
        file.write(content)


    flash(f"{filename} has been updated.")
    return redirect(url_for("index"))


@app.route("/new")
@required_sign_in
def new_document():
    return render_template("new.html")


@app.route("/create", methods=["POST"])
@required_sign_in
def create_file():
    filename = request.form.get('filename', '').strip()
    data_dir = get_data_path()
    file_path = os.path.join(data_dir, filename)

    if len(filename) == 0:
        flash("A name is required.")
        return render_template('new.html'), 422
    elif os.path.exists(file_path):
        flash(f"{filename} already exists.")
        return render_template('new.html'), 422
    else:
        with open(f"{file_path}.txt", 'w') as file:
            file.write("")
        flash(f"{filename} has been created.")
        return redirect(url_for('index'))


@app.route("/<filename>/delete", methods=["POST"])
@required_sign_in
def delete_file(filename):
    data_dir = get_data_path()
    filepath = os.path.join(data_dir, filename)
    
    if os.path.isfile(filepath):
        os.remove(filepath)
        flash(f"{filename} has been deleted")
    else:
        flash(f"{filename} does not exist.")
    
    return redirect(url_for("index"))
    


if __name__ == '__main__':
    app.run(debug=True, port=5003)