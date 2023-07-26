import React from 'react';
import MovieList from './components/movies_db';
import MovieDetails from './components/movie_info';
import MovieForm from './components/add_movie';

const App = () => {
  return (
    <div>
      <h1>Movie Management System</h1>
      <MovieList />
      <MovieDetails />
      <MovieForm />
    </div>
  );
};

export default App;
