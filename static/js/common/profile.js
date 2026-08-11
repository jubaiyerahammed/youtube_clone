document.addEventListener("DOMContentLoaded", function () {

    const profileButton =
        document.getElementById("profileButton");

    const profileMenu =
        document.getElementById("profileMenu");


    // Safety check
    if (!profileButton || !profileMenu) {
        return;
    }


    /* =====================================
       OPEN / CLOSE PROFILE MENU
    ===================================== */

    function openProfileMenu() {

        profileMenu.classList.add("open");

        profileButton.setAttribute(
            "aria-expanded",
            "true"
        );

        profileMenu.setAttribute(
            "aria-hidden",
            "false"
        );
    }


    function closeProfileMenu() {

        profileMenu.classList.remove("open");

        profileButton.setAttribute(
            "aria-expanded",
            "false"
        );

        profileMenu.setAttribute(
            "aria-hidden",
            "true"
        );
    }


    function toggleProfileMenu() {

        const isOpen =
            profileMenu.classList.contains("open");


        if (isOpen) {

            closeProfileMenu();

        } else {

            openProfileMenu();

        }
    }


    /* =====================================
       PROFILE BUTTON CLICK
    ===================================== */

    profileButton.addEventListener(
        "click",
        function (event) {

            event.stopPropagation();

            toggleProfileMenu();

        }
    );


    /* =====================================
       PREVENT MENU CLICK FROM CLOSING
    ===================================== */

    profileMenu.addEventListener(
        "click",
        function (event) {

            event.stopPropagation();

        }
    );


    /* =====================================
       CLICK OUTSIDE
    ===================================== */

    document.addEventListener(
        "click",
        function (event) {

            const clickedInsideMenu =
                profileMenu.contains(event.target);

            const clickedProfileButton =
                profileButton.contains(event.target);


            if (
                !clickedInsideMenu &&
                !clickedProfileButton
            ) {

                closeProfileMenu();

            }

        }
    );


    /* =====================================
       ESCAPE KEY
    ===================================== */

    document.addEventListener(
        "keydown",
        function (event) {

            if (event.key === "Escape") {

                closeProfileMenu();

                profileButton.focus();

            }

        }
    );

});