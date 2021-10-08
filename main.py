from flask import Flask, render_template, request
import requests

posts = requests.get("https://api.npoint.io/88c2c1f644ef334058be").json()
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", posts= posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        print(request.form['name'])
        success = True
        return render_template('contact.html', success = success)
    elif request.method == 'GET':
        success = False
        return render_template("contact.html",  success = success)

@app.route("/post/<int:id>")
def post(id):
    return render_template("post.html", posts= posts, id= id )


if __name__ == "__main__":
    app.run(debug=True)