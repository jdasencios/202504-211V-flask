from flask import render_template


def render_comment_list():
    return render_template("comment/list.html")
