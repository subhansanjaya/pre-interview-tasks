$(function(){
    	// hide latest posts when latest posts link click except first one
$("#latestposts").click(function() {

   $('.latest-posts-desc:not(:first)').toggleClass("hidden unhidden");
   $('#posts .row:not(:first)').toggleClass("hidden unhidden");
}); 

});
