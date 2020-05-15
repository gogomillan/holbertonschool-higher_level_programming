/*
  script that fetches and lists all movies title by using this URL:
  https://swapi-api.hbtn.io/api/films/?format=json
  - All movie titles are listed in the HTML tag UL#list_movies
  - It is used the jQuery API
 */
$.ajax({
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  dataType: 'text',
  success: function (data) {
    let li = '<li></li>';
    for (const movie of JSON.parse(data).results) {
      console.log(movie.title);
      li = '<li>' + movie.title + '</li>';
      $('UL#list_movies').append(li);
    }
  }
});
