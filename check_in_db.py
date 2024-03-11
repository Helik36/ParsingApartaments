import asyncio
import os
import sqlite3
import logging
import datetime

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


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

    conn.commit()
    conn.close()


if __name__ == '__main__':
    asyncio.run(create_db())
