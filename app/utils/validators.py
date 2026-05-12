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



def validate_user_json(data):
    errors = []

    if not data:
        return "", "", "", ["El cuerpo de la petición debe ser JSON."]

    username = clean_text(data.get("username"))
    email = clean_text(data.get("email"))
    password = clean_text(data.get("password"))

    if not username:
        errors.append("El username es obligatorio.")
    if not email:
        errors.append("El email es obligatorio.")
    if email and "@" not in email:
        errors.append("El email no tiene un formato válido.")
    if not password:
        errors.append("El password es obligatorio.")

    return username, email, password, errors
