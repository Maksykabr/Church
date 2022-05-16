$(document).ready(function(){
    $('.slider').slick({
        arrows:true,
        adaptiveHeight:true,
        slidesToShow:1,
        speed:1000,
        infinite:false,
        autoplay:false,
        autoplaySpeed:700,//speed for shack slides
        pauseOnFocus:true,
        pauseOnHover:true,
        draggeble:false,//Scroll mouse on the desctop
        waitForAnimation:true,//You will able to fastly switch slides if turn off this function
        //centerMode:false, // To do active slide in the center and focus on the him 
        //variableWidth:false,//Makes all content visible across the width of the screen
        //row:3     Count objects in the one slide
        //slidesPerRow:2    Count slides in the row  
        //vertical:false, //Vertical scroll. Better use with fixed height
        //asNavFor:"classAnotherSlider" Connected two sliders
    });
});