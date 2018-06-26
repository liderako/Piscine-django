from django.shortcuts import render
from django.http import HttpResponse
from .models import Movies
import psycopg2

def init(req):
    conn = psycopg2.connect(
        database="day05",
        host='localhost',
        user="asvirido",
        password='secret'
        )
    curr = conn.cursor()

    curr.execute(""" CREATE TABLE IF NOT EXISTS ex04_movies (
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

def display(requests):
    try:
        conn = psycopg2.connect(
            database="day05",
            host='localhost',
            user="asvirido",
            password='secret'
        )

        curr = conn.cursor()
        curr.execute(" SELECT * FROM ex02_movies ")
        row = curr.fetchall()
        if (len(row) == 0):
            raise Exception("No data available")
        l = list()
        for x in row:
            l.append(x)
        conn.close()
        return render(requests, "display.html", {'data': l})
    except:
        return  (HttpResponse("No data available"))


def remove(req):
    return (HttpResponse("remove"))

def populate(req):
    conn = psycopg2.connect(
        database="day05",
        host='localhost',
        user="asvirido",
        password='secret'
    )
    res = ""
    curr = conn.cursor()
    try:
        curr.execute(""" INSERT INTO ex02_movies (episode_nb, title, director, producer, release_date)
                        VALUES ('1', 'The Phantom Menace', 'George Lucas', 'Rick McCallum', '1999-05-19')
                        """)
        conn.commit()
        res += "Ok 1 "
    except psycopg2.Error as e:
        return (HttpResponse("KO 1" + str(e.pgerror)))
    try:
        curr.execute(""" INSERT INTO ex02_movies (episode_nb, title, director, producer, release_date)
                        VALUES ('2', 'Attack of the Clones', 'George Lucas', 'Rick McCallum','2002-05-16')
                        """)
        conn.commit()
        res += "Ok 2 "
    except psycopg2.Error as e:
        return (HttpResponse("KO 2" + str(e.pgerror)))
    try:
        curr.execute(""" INSERT INTO ex02_movies (episode_nb, title, director, producer, release_date)
                        VALUES ('3', 'Revenge of the Sith', 'George Lucas', 'Rick McCallum','2005-05-19')
                        """)
        conn.commit()
        res += "Ok 3 "
    except psycopg2.Error as e:
        return (HttpResponse("KO 3" + str(e.pgerror)))
    try:
        curr.execute(""" INSERT INTO ex02_movies (episode_nb, title, director, producer, release_date)
                        VALUES ('4', 'A New Hope', 'George Lucas', 'Gary Kurtz, Rick McCallum','1977-05-25')
                        """)
        conn.commit()
        res += "Ok 4 "
    except psycopg2.Error as e:
        return (HttpResponse("KO 4" + str(e.pgerror)))
    try:
        curr.execute(""" INSERT INTO ex02_movies (episode_nb, title, director, producer, release_date)
                        VALUES ('5', 'The Empire Strikes Back', 'Irvin Kershner', 'Gary Kutz, Rick McCallum','1980-05-17')
                        """)
        conn.commit()
        res += "Ok 5 "
    except psycopg2.Error as e:
        return (HttpResponse("KO 5" + str(e.pgerror)))
    try:
        curr.execute(""" INSERT INTO ex02_movies (episode_nb, title, director, producer, release_date)
                        VALUES ('6', 'Return of the Jedi', 'Richard Marquand', 'Howard G. Kazanjian, George Lucas, Rick McCallum','1983-05-25')
                        """)
        conn.commit()
        res += "Ok 6 "
    except psycopg2.Error as e:
        return (HttpResponse("KO 6" + str(e.pgerror)))
    try:
        curr.execute(""" INSERT INTO ex02_movies (episode_nb, title, director, producer, release_date)
                        VALUES ('7', 'The Force Awakens', 'J. J. Abrams', 'Kathleen Kennedy, J. J. Abrams, Bryan Burk','2015-12-11')
                        """)
        conn.commit()
        res += "Ok 7"
    except psycopg2.Error as e:
        return (HttpResponse("KO 7" + str(e.pgerror)))
    conn.close()
    return (HttpResponse(res))