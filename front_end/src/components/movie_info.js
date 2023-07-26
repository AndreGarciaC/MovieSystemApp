import React from 'react';

const MovieDetails = ({ movie }) => {
  return (
    <div>
      <h2>{title}</h2>
      <p><strong>Genre:</strong> {genre}</p>
      <p><strong>Rating:</strong> {rating}</p>
      <p><strong>Cast:</strong> {cast.join(', ')}</p>
      <p><strong>Crew:</strong> {crew.join(', ')}</p>
      <p><strong>Release Date:</strong> {releaseDate}</p>
    </div>
  );
};

export default MovieDetails;
