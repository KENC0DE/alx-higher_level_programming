$.ajax({
  type: 'GET',
  url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
  success: (greet) => {
    $('div#hello').text(greet.hello);
  }
});
