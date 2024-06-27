document.addEventListener('DOMContentLoaded', function () {
    // Select the menu lists
    // add listener to each list to check if it is clicked,
    // if clicked, find the active li and remove the active class from it.
    // add the active class to the currently clicked node
    var sidePanelList = document.querySelectorAll(".sidebar .menu li");
    sidePanelList.forEach(sidePanel => {
        sidePanel.addEventListener('click', function () {
            var activePanel = document.querySelector(".sidebar .menu li.active");
            if (activePanel) {
                activePanel.classList.remove('active');
            };
            sidePanel.classList.add('active');
        });
    });
});