import asyncio
import sqlite3
import datetime

path_db = "base_urls.db"

async def check_url_in_db(db, path):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    list_urls = [i[0] for i in cursor.execute(f"SELECT urls FROM {db}")]
    list_date = [i[0] for i in cursor.execute(f"SELECT date FROM {db}")]

    return list_urls, list_date


async def append_urls(url, db, path):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    cursor.execute(f"INSERT INTO {db} (urls, date) VALUES (?, ?)",
                   [url, datetime.datetime.now().strftime("%d-%m-%Y %H:%M")])
    conn.commit()
    conn.close()


async def append_users_id_telegram(id_user, path):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    cursor.execute(f"INSERT INTO chat_id_users (users_id) VALUES (?)", [id_user])
    conn.commit()
    conn.close()


async def get_users_id_telegram(path):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    user_id_telegram = [i[0] for i in cursor.execute("SELECT users_id FROM chat_id_users")]
    conn.close()

    return user_id_telegram


async def append_new_url_from_pars(url, path):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    cursor.execute(f"INSERT INTO new_urls_pars (urls) VALUES (?)", [url])
    conn.commit()
    conn.close()


async def get_new_url_from_pars(path):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    get_new_url = [i[0] for i in cursor.execute(f"SELECT urls FROM new_urls_pars")]
    conn.close()

    return get_new_url


async def detele_new_url(path):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    cursor.execute(f"DELETE FROM new_urls_pars")
    conn.commit()
    conn.close()


async def delete_users_id_telegram(path):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM chat_id_users WHERE users_id = 1005555225")

    conn.commit()
    conn.close()

async def app_users_id_telegram(path, id):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO chat_id_users (users_id) VALUES (?)", [id])

    conn.commit()
    conn.close()

async def delete_urls_from_table(path):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM urls_rooms_db")

    conn.commit()
    conn.close()


async def create_db():
    conn = sqlite3.connect('base_urls.db')
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS urls_apartment_db(
    id INTEGER PRIMARY KEY,
    urls TEXT NOT NULL,
    date TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS urls_section_db(
    id INTEGER PRIMARY KEY,
    urls TEXT NOT NULL,
    date TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS urls_rooms_db(
    id INTEGER PRIMARY KEY,
    urls TEXT NOT NULL,
    date TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS urls_lands_db(
    id INTEGER PRIMARY KEY,
    urls TEXT NOT NULL,
    date TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chat_id_users(
    id INTEGER PRIMARY KEY,
    users_id TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS new_urls_pars(
    id INTEGER PRIMARY KEY,
    urls TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()
