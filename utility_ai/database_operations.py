import sqlite3
from typing import Union


def get_user_config(key: str) -> Union[bool, tuple]:
    connection = sqlite3.connect('utility_ai.sqlite', isolation_level=None)
    cursor = connection.cursor()

    cursor.execute("SELECT configuration FROM users WHERE key=?", (key,))
    result = cursor.fetchone()

    return result


def create_user(key: str, configuration: str) -> bool:
    connection = sqlite3.connect('utility_ai.sqlite', isolation_level=None)
    cursor = connection.cursor()

    try:
        create_table = "CREATE TABLE IF NOT EXISTS users(key TEXT PRIMARY KEY, configuration TEXT UNIQUE)"
        cursor.execute(create_table)

        create = "INSERT INTO users VALUES (?,?)"
        cursor.execute(create, (key, configuration))
    except:
        return False

    return True
