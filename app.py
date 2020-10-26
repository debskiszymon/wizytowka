from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def main():
    return redirect("/mypage/me")

@app.route("/mypage/")
def mypage():
    return redirect("/mypage/me")

@app.route("/mypage/me")
def parent():
    return render_template ("me.html")

@app.route("/mypage/contact", methods=["GET", "POST"])
def child():
    if request.method == "GET":
        items = ["EMAIL: debsk@pl", "Telefon: 600600600"]
        return render_template ("contact.html", items=items)
    elif request.method == "POST":
        print(request.form.getlist('message')[0])
        message = request.form.getlist('message')[0]
        return render_template("message.html", message=message)
