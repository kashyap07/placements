$('#menu-action').click(function() {
  console.log("hi");
  $('.sidebar').toggleClass('active');
  $('.main').toggleClass('active');
  $(this).toggleClass('active');

  if ($('.sidebar').hasClass('active')) {
    $(this).find('i').addClass('fa-close');
    $(this).find('i').removeClass('fa-bars');
  } else {
    $(this).find('i').addClass('fa-bars');
    $(this).find('i').removeClass('fa-close');
  }
});

$(".sidebar a").click(function () {
    if(!$(this).hasClass('active')){
      console.log(this);
      $(".sidebar a").removeClass('active');
      $(this).addClass('active')
    }
    console.log(this);
});

// Add hover feedback on menu
$('#menu-action').hover(function() {
    $('.sidebar').toggleClass('hovered');
}); 