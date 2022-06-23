/* Toggle between showing and hiding the navigation menu links when the user clicks on the hamburger menu / bar icon */
function showMobile() {
    var x = document.getElementById("myLinks");
    if (x.style.display == "block") {
        x.style.display = "none";
    } else {
        x.style.display = "block";
    }
}


// d-md-flex justify-content-md-end d-md-block