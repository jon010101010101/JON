from django.shortcuts import render, HttpResponse
from django.db import connections

def init(request):
    try:
        with connections['default'].cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ex00_movies (
                    title VARCHAR(64) UNIQUE NOT NULL,
                    episode_nb INTEGER PRIMARY KEY,
                    opening_crawl TEXT,
                    director VARCHAR(32) NOT NULL,
                    producer VARCHAR(128) NOT NULL,
                    release_date DATE NOT NULL
                );
            """)
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error: {e}")
