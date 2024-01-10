const list = $('ul.my_list');

$('div#add_item').click(() => {
  list.append('<li>Item</li>');
});
