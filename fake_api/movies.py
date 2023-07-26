movies = [
    {
        "title": "Titanic II",
        "rating": 6.8,
        "genre": "Drama",
        "cast": ["Actor A", "Actress B", "Actor C"],
        "releaseDate": "2023-05-15"
    },
    {
        "title": "Laugh Out Loud",
        "rating": 7.2,
        "genre": "Comedy",
        "cast": ["Actor X", "Actress Y", "Actor Z"],
        "releaseDate": "2023-08-21"
    },
    {
        "title": "Chilling Fear",
        "rating": 8.1,
        "genre": "Horror",
        "cast": ["Actor D", "Actress E"],
        "releaseDate": "2023-10-31"
    },
    {
        "title": "Mind Games",
        "rating": 9.0,
        "genre": "Thriller",
        "cast": ["Actor F", "Actress G", "Actor H", "Actress I"],
        "releaseDate": "2023-06-18"
    },
    {
        "title": "Unbreakable Bonds",
        "rating": 8.5,
        "genre": "Action",
        "cast": ["Actor J", "Actress K"],
        "releaseDate": "2023-09-08"
    }
]
#JSON SCHEMA
# { "title": { "type": "string", "minLength": 1, "maxLength": 255 }, 
# "rating": { "type": "number", "minimum": 0, "maximum": 10 },
# "genre": { "type": "string", "enum": ["Action", "Comedy", "Drama", "Horror", "Thriller"] },
# "cast": { "type": "array", "items": { "type": "string" } },
# "releaseDate": { "type": "string", "format": "date" } }
