/*
  script that fetches from https://fourtonfish.com/hellosalut/?lang=fr and
  displays the value of hello from that fetch in the HTMLs tag DIV#hello.
  - The translation of hello must be display in the HTML tag DIV#hello
  - It is used the jQuery API
  - Your script must work when it is imported from the HEAD tag
 */
$.ajax({
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  dataType: 'text',
  success: function (data) {
    $('DIV#hello').text(JSON.parse(data).hello);
  }
});
