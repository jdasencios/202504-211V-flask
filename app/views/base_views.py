from flask import render_template


def render_root():
    return render_template("base.html")


def render_home():
    return render_template("home.html")
