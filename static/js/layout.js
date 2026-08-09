const sidebar = document.getElementById("sidebar");
const main = document.querySelector(".main");

document.querySelectorAll(".menu-toggle").forEach(btn => {
    btn.addEventListener("click", () => {
        sidebar.classList.toggle("collapsed");
        main.classList.toggle("collapsed");
    });
});
