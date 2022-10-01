from distutils.log import debug
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "%sqlite://database/au_bon_pain.db"
db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug=True)

menu = []

@app.route("/")
def index():
    return render_template("index.html", num_posts=len(menu))

"""
@app.route("/p/<string:slug>/")
def show_post(slug):
    return render_template("post_view.html", slug_title=slug)



@app.route("/admin/post/")
@app.route("/admin/post/<int:post_id>/")
def post_form(post_id=None):
    return render_template("admin/post_form.html", post_id=post_id)

"""