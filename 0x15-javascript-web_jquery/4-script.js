window.$('#toggle_header').click(function () {
  if (window.$('header').hasClass('green')) {
    window.$('header').addClass('red').removeClass('green');
  } else {
    window.$('header').addClass('green').removeClass('red');
  }
});
