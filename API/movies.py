from flask import Flask, jsonify, request

app = Flask(__name__)
movies = [
    {
        "name": "Captain America: The First Avenger",
        "casts": ["Chris Evans", "Tommy Lee Jones"],
        "genres": ["Action","Fiction"]
    },
    {
        "name": "Spider-Man: Homecoming",
        "casts": ["Tom Holland","Michael Keaton"],
        "genres": ["Action","Fiction"]
    }
]

@app.route('/movies', methods=['GET'])
def getMovies():
    return jsonify(movies)

if __name__ == '__main__':
    app.run()