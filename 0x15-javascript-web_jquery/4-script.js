$('div#toggle_header').click(() => {
  const header = $('header');
  if (header.hasClass('green')) {
    header.removeClass('green').addClass('red');
  } else {
    header.removeClass('red').addClass('green');
  }
});
