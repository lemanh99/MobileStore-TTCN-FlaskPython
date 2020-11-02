$(document).ready(function(){
    $('.owl-one').owlCarousel({
        loop:true,
    margin:0,
    autoplay:true,
    autoplayTimeout:3000,
   Item_Width : 100,
    nav:true,
    navText:['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right "></i>'],
        responsive: {
            0: {
                items: 1,
                
            },
            600: {
                items: 1,
                
            },
            1000: {
                items: 1,
                
            },
            1200: {
                items: 1,
                
            },
            1400: {
                items: 1,
                
            },
            1600: {
                items: 1,
                
            },
            1800: {
                items: 1,
                
            }
        }
    });

    $('.owl-two').owlCarousel({

    loop:true,
    margin:0,
    autoplay:true,
    autoplayTimeout:3000,
    dots:false,
    nav:true,
    navText:['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right "></i>'],
        responsive:{
            0:{
                items:1
            },
            600:{
                items:2
            },
            1000:{
                items:4
            }
        }
    });

 $('.owl-three').owlCarousel({

       loop:true,
    margin:0,
    autoplay:true,
    autoplayTimeout:3000,

    nav:false,

        responsive:{
            0:{
                items:1
            },
            600:{
                items:1
            },
            1000:{
                items:2
            }
        }
    });
 $('.owl-Four').owlCarousel({

       loop:true,
    margin:0,
    autoplay:true,
    autoplayTimeout:3000,

    nav:false,
    navText:['<i class="icon-back-2"></i>', '<i class="icon-next-4"></i>'],
        responsive:{
            0:{
                items:1
            },
            600:{
                items:1
            },
            1000:{
                items:1
            }
        }
    });






    
});