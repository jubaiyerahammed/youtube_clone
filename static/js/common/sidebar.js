document.addEventListener("DOMContentLoaded", function () {

    const menuToggle = document.getElementById("menuToggle");

    if (!menuToggle) {
        return;
    }

    menuToggle.addEventListener("click", function () {

        document.body.classList.toggle("sidebar-collapsed");

    });

});