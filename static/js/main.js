console.log('main.js загружен');

$(document).ready(function(){
    console.log('DOM готов, инициализация Slick');

    console.log('slider-for найден:', $('.slider-for').length);
    console.log('slider-nav найден:', $('.slider-nav').length);
    $('.slider-for').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        fade: true,
        asNavFor: '.slider-nav'
    });
    
    $('.slider-nav').slick({
        slidesToShow: 3,
        slidesToScroll: 1,
        asNavFor: '.slider-for',
        dots: true,
        centerMode: true,
        focusOnSelect: true
    });
});