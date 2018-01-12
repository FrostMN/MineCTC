from flask import Flask, render_template, send_file

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route("/downloads/mods/<path>")
def download_mod(path=None):
    if path is None:
        return "400"
    try:
        print("in try")
        print(path)
        file_path = "static/downloads/mods/" + str(path)
        return send_file(file_path, as_attachment=True)
    except Exception as e:
        # self.log.exception(e)
        # self.Error(400)
        print(str(e))
        return "400"


@app.route("/downloads/forge/<file>")
def download_modload(file=None):
    if file is None:
        return "400"
    try:
        print("in try")
        print(file)
        file_path = "static/downloads/forge/" + file
        return send_file(file_path, as_attachment=True)
    except Exception as e:
        # self.log.exception(e)
        # self.Error(400)
        print(str(e))
        return "400"


if __name__ == '__main__':
    app.run()
