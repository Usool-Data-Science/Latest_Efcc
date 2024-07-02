document.addEventListener('DOMContentLoaded', function () {
    var rows = document.querySelectorAll("table tbody tr");

    rows.forEach(function (row) {
        row.addEventListener('click', function () {
            var petitionId = this.getAttribute("data-petition-id");

            if (petitionId) {
                window.location.href = "/petitions/" + petitionId;
            }
        });
    });
});