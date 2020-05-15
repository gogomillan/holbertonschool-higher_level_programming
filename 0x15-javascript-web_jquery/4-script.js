/*
  script that toggles the class of the HTML tag HEADER to red (#FF0000) when
  the user clicks on the tag DIV#toggle_header:
  - The HEADER tag must always have one class: red or green, never both in the
    same time, never empty.
  - If the current class is red, when the user click on DIV#toggle_header, the
    class must be updated to green ; and the reverse.
  - It is used the jQuery API
 */
$('DIV#toggle_header').click(function () {
  if ($('header').attr('class') === 'green') {
    $('header').removeClass('green');
    $('header').addClass('red');
  } else {
    $('header').removeClass('red');
    $('header').addClass('green');
  }
});
