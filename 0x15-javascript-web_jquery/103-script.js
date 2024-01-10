function translate() {
    const frmt = 'https://hellosalut.stefanbohacek.dev/?lang=';
    const full_url = frmt + $('input#language_code').val();
    $.ajax({
      type: 'POST',
      url: full_url,
      success: (greet) => {
        $('div#hello').text(greet.hello);
      }
    });
  }

window.onload = () => {
  $('input#btn_translate').click(() => {
    translate();
  })

  $('input#language_code').keydown((event) => {
    if (event.key === 'Enter') {
      translate();
    }
  })
};
