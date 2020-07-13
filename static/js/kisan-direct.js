
// https://stackoverflow.com/questions/8579643/how-to-scroll-up-or-down-the-page-to-an-anchor-using-jquery
function scrollToAnchor(aname){
    var aTag = $("a[name='"+ aname +"']");
    $('html,body').animate({scrollTop: aTag.offset().top},'slow');
}