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

$(document).ready(function () {
    var maxField = 20; //Input fields increment limitation
    var addButton = $('.add_button_drinks'); //Add button selector
    var wrapper = $('.field_wrapper_drinks'); //Input field wrapper
    var fieldHTML =
        '<div class="d-flex flex-row mb-1"><label class="mr-2">Discrption:</label><input type="text" name="field_name[]" value="" class="form-control" /><label class="mx-2">Price:</label><input type="text" name="field_name[]" value="" class="form-control"/><a href="javascript:void(0);" class="remove_button m-1" title="Add field"><img class="" src="img/icons8-delete-64.png" height="30px" width="30px" /></a></div>'; //New input field html 
    var x = 1; //Initial field counter is 1

    //Once add button is clicked
    $(addButton).click(function () {
        //Check maximum number of input fields
        if (x < maxField) {
            x++; //Increment field counter
            $(wrapper).append(fieldHTML); //Add field html
        }
    });

    //Once remove button is clicked
    $(wrapper).on('click', '.remove_button', function (e) {
        e.preventDefault();
        $(this).parent('div').remove(); //Remove field html
        x--; //Decrement field counter
    });
});