import asyncio
import os
import sqlite3
import datetime


async def check_url_in_db(db):
    conn = sqlite3.connect('database/base_urls.db')
    cursor = conn.cursor()

    list_urls = [i[0] for i in cursor.execute(f"SELECT urls FROM {db}")]
    list_date = [i[0] for i in cursor.execute(f"SELECT date FROM {db}")]

    return list_urls, list_date


async def append_urls(url, db):
    conn = sqlite3.connect('database/base_urls.db')
    cursor = conn.cursor()

    cursor.execute(f"INSERT INTO {db} (urls, date) VALUES (?, ?)",
                   [url, datetime.datetime.now().strftime("%d-%m-%Y %H:%M")])
    conn.commit()
    conn.close()


async def append_users_id_telegram(id_user):
    conn = sqlite3.connect('database/base_urls.db')
    cursor = conn.cursor()

    cursor.execute(f"INSERT INTO chat_id_users (users_id) VALUES (?)", [id_user])
    conn.commit()
    conn.close()


async def get_users_id_telegram():
    conn = sqlite3.connect('database/base_urls.db')
    cursor = conn.cursor()

    user_id_telegram = [i[0] for i in cursor.execute("SELECT users_id FROM chat_id_users")]
    conn.close()

    return user_id_telegram


async def append_new_url_from_pars(url):
    conn = sqlite3.connect('database/base_urls.db')
    cursor = conn.cursor()

    cursor.execute(f"INSERT INTO new_urls_pars (urls) VALUES (?)", [url])
    conn.commit()
    conn.close()

async def get_new_url_from_pars():
    conn = sqlite3.connect('database/base_urls.db')
    cursor = conn.cursor()

    get_new_url = [i[0] for i in cursor.execute(f"SELECT urls FROM new_urls_pars")]
    conn.close()

    return get_new_url

async def detele_new_url():
    conn = sqlite3.connect('database/base_urls.db')
    cursor = conn.cursor()

    cursor.execute(f"DELETE FROM new_urls_pars")
    conn.commit()
    conn.close()


async def create_db():
    try:
        os.mkdir("database")
    except FileExistsError:
        pass

    conn = sqlite3.connect('database/base_urls.db')
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


if __name__ == '__main__':
    asyncio.run(create_db())

    # conn = sqlite3.connect('database/base_urls.db')
    # cursor = conn.cursor()
    #
    # cursor.execute(f"DROP TABLE chat_id_users")
    # conn.commit()
    # conn.close()

