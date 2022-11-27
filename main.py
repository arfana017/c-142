from flask import Flask, jsonify, request
from storage import all_movies, liked_movies, unliked_movies, did_not_watch
from demographic_filtering import output
from content_filtering import get_recommendations

app = Flask(__name__)

@app.route("/get-movie")
def get_movie():
    movie_data = {
        'title': all_movies[0][19],
        'poster_link': all_movies[0][27],
        'released_date': all_movies[0][13] or 'N/A',
        'duration': all_movies[0][15],
        'rating': all_movies[0][20],
        'overview': all_movies[0][9]
    }
    return jsonify({
        "data": movie_data,
        "status": "success"
    })

@app.route("/liked-movie", methods = ["POST"])
def liked_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    liked_movies.append(movie)
    return jsonify({
        "status": "success"
    })

@app.route("/unliked-movie", methods = ["POST"])
def unliked_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    unliked_movies.append(movie)
    return jsonify({
        "status": "success"
    })

@app.route("/did-not-watch", methods = ["POST"])
def did_not_watch():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    did_not_watch.append(movie)
    return jsonify({
        "status": "success"
    })

@app.route('/popular-movies')
def popular_movies():
    movie_data = []
    for movie in output:
        data = {
            'title': movie[0],
            'poster_link': movie[1],
            'release_date': movie[2] or 'N/A',
            'duration': movie[3],
            'rating': movie[4],
            'overview': movie[5]
        }
        movie_data.append(data)
    return jsonify({
        "data": movie_data,
        "status": "success"
    })

@app.route('/recommended-movies')
def recommended_movies():
    all_recommended = []
    for liked_movie in liked_movies:
        output = get_recommendations(liked_movies[19])
        for data in output:
            all_recommended.append(data)
    all_recommended.sort()
    movie_data = []
    for recommended in all_recommended:
        data = {
            'title': recommended[0],
            'poster_link': recommended[1],
            'release_date': recommended[2] or 'N/A',
            'duration': recommended[3],
            'rating': recommended[4],
            'overview': recommended[5]
        }
        movie_data.append(data)
    return jsonify({
        'data': movie_data,
        'status': 'success'
    })

if __name__ == "__main__":
    app.run()