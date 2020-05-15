/*
  script that adds a LI element to a list when the user clicks on the tag DIV#add_item:
  - The new element is: <li>Item</li>
  - The new element is added to UL.my_list
  - It is used the jQuery API
 */
$('DIV#add_item').click(function () {
  $('UL.my_list').append('<li>Item</li>');
});
