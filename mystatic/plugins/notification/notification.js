// Gameforest notification plugin by yakuzi
// Author: https://yakuthemes.com
// Version: 1.0

$.fn.notification = function(notify) {

  $(this).click(function(e) {
    e.preventDefault();

    var id = 1 + Math.floor(Math.random() * 99);
    var title = $(this).data("title");

    if ($(this).data("notification")) {
      var alert = $(this).data("notification");
    } else {
      var alert = 'info';
    }

    if ($(this).data("alignment")) {
      var align = 'notification-' + $(this).data("alignment");
    } else {
      var align = '';
    }

    $('body').append('<div id="notification-' + id + '" class="notification ' + align + ' animated fadeInDown fast"><div class="alert alert-' + alert + '">' + title + '</div></div>');

    setTimeout(function(){
  		$('body').find('#notification-' + id).removeClass('fadeInDown');
  		$('body').find('#notification-' + id).addClass('fadeOutUp');
  	}, 3000);

  	setTimeout(function(){
  		$('body').find('#notification-' + id).remove();
  	}, 4000);
  });

  return this;
};
