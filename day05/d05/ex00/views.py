from django.shortcuts import render
from django.http import HttpResponse
import psycopg2

def     index(requests):
    conn = psycopg2.connect(
        database="day05",
        host='localhost',
        user="asvirido",
        password='secret'
        )
    curr = conn.cursor()

    curr.execute(""" CREATE TABLE IF NOT EXISTS ex00_movies (
            title varchar(64) NOT NULL,
            episode_nb integer PRIMARY KEY,
            open_crawl text,
            director varchar(32) NOT NULL,
            producer varchar(128) NOT NULL,
            release_date date NOT NULL
            )
            """)
    conn.commit()
    conn.close()
    return (HttpResponse("Ok"))