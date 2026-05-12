from flask import render_template


def render_post_list(posts):
    return render_template("post/list.html", post_list=posts)


def render_post_list_partial(posts):
    return render_template("partials/datos-json.html", post_list=posts)


def render_post_detail(post):
    return render_template("post/single.html", post_single=post)


def render_post_create_form(errors=None):
    return render_template("post/create.html", errors=errors or [])


def render_post_update_form(post, errors=None):
    return render_template("post/update.html", single_post=post, errors=errors or [])
