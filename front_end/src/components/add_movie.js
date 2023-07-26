import React, { useState } from 'react';
import axios from 'axios';

const MovieForm = () => {
  const [title, setTitle] = useState('');
  const [genre, setGenre] = useState('');


  const handleSubmit = (e) => {
    e.preventDefault();
    const newMovie = { title, genre }; // Add more movie properties here
    axios.post('http://localhost:5000/api/movies', newMovie)
      .then(response => console.log(response.data))
      .catch(error => console.error(error));
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="title">Title:</label>
        <input
          type="text"
          id="title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
        />
      </div>
      <div>
        <label htmlFor="genre">Genre:</label>
        <input
          type="text"
          id="genre"
          value={genre}
          onChange={(e) => setGenre(e.target.value)}
          required
        />
      </div>
      <div>
        <button type="submit">Add Movie</button>
      </div>
    </form>
  );
};

export default MovieForm;
