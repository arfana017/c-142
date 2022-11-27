import csv

all_movies = []
with open("final.csv", encoding="utf8") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

liked_movies = []
unliked_movies = []
did_not_watch = []