$( document ).ready(function(){$(".button-collapse").sideNav();})


  $(document).ready(function(){
    $('.collapsible').collapsible();
  });




$(document).ready(function(){
 $('.owl-carousel').owlCarousel({
    loop:true,
    margin:0,
    nav:false,
    navText:["<", ">"],
    autoplay:true,
    autoplayTimeout:2000,
    responsiveClass:true,
    responsive:{
        0:{
            items:2,
            nav:false
        },
        600:{
            items:4,
            nav:false
        },
        1000:{
            items:5,
            nav:false,
            loop:true,
        }
    }
}) ;
})
