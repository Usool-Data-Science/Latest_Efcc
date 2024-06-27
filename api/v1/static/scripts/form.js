document.addEventListener('DOMContentLoaded', function () {
    var formSwitches = document.querySelectorAll("#formSwitch");

    formSwitches.forEach(function (formSwitch) {
        var initialLabel = formSwitch.textContent;
        formSwitch.addEventListener('click', function () {
            var dataID = this.getAttribute("data-id");
            var formContent = document.querySelector("#" + dataID);

            if (formContent.classList.contains('hidden')) {
                this.textContent = "Close Form Page";
                formContent.classList.remove('hidden');
            } else {
                this.textContent = initialLabel;
                formContent.classList.add('hidden');
            }
        });
    });
});
