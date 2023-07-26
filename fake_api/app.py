from flask import Flask, jsonify, request 
'''Jsonify permite convertir un objeto a un json típico del navegador. 
Request es un objeto de flask que proporciona los datos enviados a través de peticiones http.
'''

app = Flask(__name__)

#Create routes
from movies import movies


@app.route('/api/movies', methods=['GET'])
def get_all_movies():
    """
    Endpoint to get all movies.
    """
    return jsonify(movies)

@app.route('/api/movies/<string:title>', methods=['GET'])
def get_movie_by_title(title):
    """
    Endpoint to get movie details by title.
    """
    for movie in movies:
        if movie['title'] == title:
            return jsonify(movie)
    return jsonify({"message": "Movie not found"}), 404

@app.route('/api/movies', methods=['POST'])
def add_movie():
    """
    Endpoint to add a new movie.
    """
    new_movie = {
        "title": request.json['title'],
        "rating": request.json['rating'],
        "genre": request.json['genre'],
        "cast": request.json['cast'],
        "releaseDate": request.json['releaseDate']
    }
    movies.append(new_movie)
    return jsonify({"message":"Movie added succesfully", "movies": movies}),201


@app.route('/api/movies/<string:title>', methods=['DELETE'])
def remove_movie(title):
    """
    Endpoint to remove a movie.
    """
    movie_found = [movie for movie in movies if movie['name']==movie_name]
    if len(movie_found)>0:
        movies.remove(movie_found[0])
        return jsonify({"message":"movie deleted","movie":movies })
    return jsonify({"message": "Movie removed successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)