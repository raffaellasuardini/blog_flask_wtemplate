from flask import Flask, render_template, request
import requests
import smtplib

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
        with smtplib.SMTP(my_smtp) as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject: New message from your blog \n\n "
                    f"name: {request.form['name']} \n"
                    f"email: {request.form['email']} \n"
                    f"phone: {request.form['phone']} \n"
                    f"message: {request.form['message']} \n"
            )
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