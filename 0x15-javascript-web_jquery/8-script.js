const list = $('ul#list_movies');
$.ajax({
  type: 'GET',
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  success: (movies) => {
    $.each(movies.results, (idx, movie) => {
      list.append('<li>' + movie.title + '</li>');
    });
  }
});
