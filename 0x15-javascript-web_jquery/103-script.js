/*
  script that fetches and prints how to say Hello depending of the language
  - It is used this API service: https://www.fourtonfish.com/hellosalut/hello/
  - The language code is the value entered in the tag INPUT#language_code
    (ex: es, fr, en etc.)
  - The translation is fetch when the user clicks on INPUT#btn_translate OR
    presses ENTER when the focus is on INPUT#language_code
  - The translation of Hello is displayed in the HTML tag DIV#hello
  - It is used the jQuery API
  - The script works when it imported from the HEAD tag
*/
$(document).ready(function () {
  function translate () {
    $.ajax({
      url: 'https://fourtonfish.com/hellosalut/?lang=' + $('INPUT#language_code').val(),
      dataType: 'text',
      success: function (data) {
        $('DIV#hello').html(JSON.parse(data).hello);
      }
    });
  }
  $('INPUT#btn_translate').click(function () {
    translate();
  });
  $('INPUT#language_code').keyup(function (event) {
    if (event.keyCode === 13) {
      translate();
    }
  });
});
