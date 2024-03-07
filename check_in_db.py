import asyncio
import os
import sqlite3


async def check_url_in_db():
    conn = sqlite3.connect('database/base_urls.db')
    cursor = conn.cursor()

    list_urls = [i[0] for i in cursor.execute("SELECT urls FROM urls_db")]

    return list_urls


async def append_urls(url):
    conn = sqlite3.connect('database/base_urls.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO urls_db (urls) VALUES (?)", [url])
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
    CREATE TABLE IF NOT EXISTS urls_db(
    id INTEGER PRIMARY KEY,
    urls TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


if __name__ == '__main__':
    asyncio.run(create_db())
