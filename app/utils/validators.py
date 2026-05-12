def clean_text(value):
    return value.strip() if value else ""


def validate_post_form(form):
    title = clean_text(form.get("title_title"))
    content = clean_text(form.get("content_content"))

    errors = []
    if not title:
        errors.append("El título es obligatorio.")
    if not content:
        errors.append("El contenido es obligatorio.")

    return title, content, errors
