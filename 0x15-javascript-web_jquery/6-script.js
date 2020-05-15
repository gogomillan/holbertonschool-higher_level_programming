/*
  script that updates the text of the HTML tag HEADER to New Header!!! when
  the user clicks on DIV#update_header
  - It is used the jQuery API
 */
$('DIV#update_header').click(function () {
  $('header').text('New Header!!!');
});
