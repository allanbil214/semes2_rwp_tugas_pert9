from flask import Flask, redirect, render_template, request, url_for, flash, session
from model import Model

app = Flask(__name__)
app.config["SECRET_KEY"] = "123"
db = Model()

@app.route("/")
def index():
    item = db.read()
    return render_template("index.html", dItem = item)

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/add_save", methods=["POST", "GET"])
def add_save():
    if(request.method == "POST"):
        id = request.form["txtID"]
        name = request.form["txtName"]
        rarity = request.form["rarity"]
        affinity = py -
        itype = request.form["itemType"]
        desc = request.form["txtDesc"]
        if(db.add(id, name, rarity, affinity, itype, desc)):
            flash("New Data have been Added")
        else:
            flash("Error detected, data can't be added!")
        return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))

@app.route("/remove/<int:id>", methods=["GET", "POST"])
def remove(id):
    if(request.method == "GET"):
        if(db.remove(id)):
            flash("The Data have been Deleted")
        else:
            flash("Error detected, data can't be deleted!")
        return redirect(url_for("index"))

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    session["edit"] = id
    getted = db.edit(id)
    return render_template(
        "edit.html",
        pData = getted,
        oldID = id)

@app.route("/edit_save", methods=["POST"])
def edit_save():
    if(request.method == "POST"):
        id = request.form["txtID"]
        name = request.form["txtName"]
        rarity = request.form["rarity"]
        affinity = ', '.join(request.form.getlist('affinity'))
        itype = request.form["itemType"]
        desc = request.form["txtDesc"]
        if(db.edit_save(id, name, rarity, affinity, itype, desc, session["edit"])):
            flash("The Data have been Edited")
        else:
            flash("Error detected, data can't be edited!")
        return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)