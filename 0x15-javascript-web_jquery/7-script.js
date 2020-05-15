/*
  script that fetches and replaces the name of this URL:
  https://swapi-api.hbtn.io/api/people/5/?format=json
  - The name is displayed in the HTML tag DIV#character
  - It is used the jQuery API
 */
$.ajax({
  url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
  dataType: 'text',
  success: function (data) {
    $('DIV#character').text(JSON.parse(data).name);
  }
});
