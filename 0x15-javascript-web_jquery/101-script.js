/*
  script that adds, removes and clears LI elements from a list when the user clicks:
  - The new element is: <li>Item</li>
  - The new element is added to UL.my_list
  - When the user clicks on DIV#add_item: a new element is added to the list
  - When the user clicks on DIV#remove_item: a last element is removed to the list
  - When the user clicks on DIV#clear_list: all elements of the list are removed
  - It is used the jQuery API
  - The script works when it imported from the HEAD tag
 */
$(document).ready(function () {
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('DIV#remove_item').click(function () {
    const list = $('ul.my_list li');
    if (list.length > 0) {
      list[list.length - 1].remove();
    }
  });
  $('DIV#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
