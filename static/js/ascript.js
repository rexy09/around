/* **************** SIDE NAVIGATION SCRIPT ********************/

/* Set the width of the side navigation to 250px and the left margin of the page content to 250px and add a black background color to body */
function openNav() {
    document.getElementById("mySidenavv").style.width = "250px";

}

/* Set the width of the side navigation to 0 and the left margin of the page content to 0, and the background color of body to white */
function closeNav() {
    document.getElementById("mySidenavv").style.width = "0";
    document.body.style.backgroundColor = "white";
}


/* **************** SIDE NAVIGATION SCRIPT FOR SETTING IN USER PROFILE ********************/

/* Set the width of the side navigation to 250px and the left margin of the page content to 250px and add a black background color to body */
function openNavSet() {
    document.getElementById("mySidenavvset").style.width = "250px";
}

/* Set the width of the side navigation to 0 and the left margin of the page content to 0, and the background color of body to white */
function closeNavSet() {
    document.getElementById("mySidenavvset").style.width = "0";
    document.body.style.backgroundColor = "white";
}


// ************** Gallery Script *****************
var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
    showSlides(slideIndex += n);
}

function currentSlide(n) {
    showSlides(slideIndex = n);
}

function showSlides(n) {
    var i;
    var slides = "";
    var slides = document.getElementsByClassName("mySlidess");

    if (n > slides.length) {
        slideIndex = 1
    }
    if (n < 1) {
        slideIndex = slides.length
    }
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }

    slides[slideIndex - 1].style.display = "block";

}