from app.db.database import get_db_connection


def row_to_dict(row):
    if row is None:
        return None
    user = dict(row)
    user.pop("password", None)
    return user


def get_all_users():
    db = get_db_connection()
    return db.execute(
        "SELECT id, username, email FROM users ORDER BY id DESC;"
    ).fetchall()


def get_user_by_id(user_id):
    db = get_db_connection()
    return db.execute(
        "SELECT id, username, email FROM users WHERE id = ?;",
        (user_id,),
    ).fetchone()


def get_user_by_email(email):
    db = get_db_connection()
    return db.execute(
        "SELECT id, username, email FROM users WHERE email = ?;",
        (email,),
    ).fetchone()


def create_user(username, email, password):
    db = get_db_connection()
    cursor = db.execute(
        "INSERT INTO users (username, email, password) VALUES (?, ?, ?);",
        (username, email, password),
    )
    db.commit()
    return cursor.lastrowid


def update_user(user_id, username, email, password):
    db = get_db_connection()
    db.execute(
        """
        UPDATE users
        SET username = ?, email = ?, password = ?
        WHERE id = ?;
        """,
        (username, email, password, user_id),
    )
    db.commit()


def delete_user(user_id):
    db = get_db_connection()
    db.execute("DELETE FROM users WHERE id = ?;", (user_id,))
    db.commit()
