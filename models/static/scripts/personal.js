document.addEventListener("DOMContentLoaded", function () {
    var formIcons = document.querySelectorAll(".modifier");
    var previewIcons = document.querySelectorAll(".previewer");

    formIcons.forEach((icon) => {
        icon.addEventListener("click", function () {
            // Retrieve its data-id, show it and change the icon
            var formId = icon.getAttribute("data-id");
            var form = document.getElementById(formId);

            // Now show the form and change the eye to eye-slash icon
            if (form) {
                if (form.classList.contains("d-none")) {
                    // Change the eye to eye-slash and show it.
                    this.innerHTML = '<i class="fa-solid fa-circle-stop"></i>';
                    form.classList.remove("d-none");
                }
                else {
                    this.innerHTML = '<i class="fa-solid fa-pen"></i>';
                    form.classList.add("d-none");
                }
            }
        });
    });

    previewIcons.forEach((icon) => {
        icon.addEventListener("click", function () {
            // Retrieve its data-id, show it and change the icon
            var previewId = icon.getAttribute("data-id");
            var preview = document.getElementById(previewId);

            // Now show the preview and change the eye to eye-slash icon
            if (preview) {
                if (preview.classList.contains("d-none")) {
                    // Change the eye to eye-slash and show it.
                    this.innerHTML = '<i class="fa-solid fa-eye-slash"></i>';
                    preview.classList.remove("d-none");
                }
                else {
                    this.innerHTML = '<i class="fa-solid fa-eye"></i>';
                    preview.classList.add("d-none");
                }
            }
        });
    });
});

/* document.addEventListener('DOMContentLoaded', function () {
    var personalIcons = document.querySelectorAll(".modifier");
    var personalPreviews = document.querySelectorAll(".previewer");
    var isMediumScreen = window.innerWidth >= 768 && window.innerWidth <= 991;
    // var isSmallScreen = window.innerWidth >= 576 && window.innerWidth <= 767;
    // var isLargeScreen = window.innerWidth >= 992;

    personalIcons.forEach(function (icon) {
        icon.addEventListener('click', function () {
            var formId = this.getAttribute("data-id");
            var form = document.getElementById(formId);

            if (form && form.classList.contains("d-none")) {
                if (isMediumScreen) {
                    this.innerHTML = '<i class="fa-solid fa-circle-stop"></i>';
                } else {
                    this.textContent = "Close Form";
                }
                form.classList.remove("d-none");
            }
            else if (form) {
                if (isMediumScreen) {
                    this.innerHTML = '<i class="fa-solid fa-pen"></i>';
                } else {
                    this.textContent = "Update";
                }
                form.classList.add("d-none");
            };
        });
    });

    personalPreviews.forEach((preview) => {
        preview.addEventListener('click', function () {
            var previewId = this.getAttribute("data-id");
            var preview = document.getElementById(previewId);

            if (preview && preview.classList.contains("d-none")) {
                if (isMediumScreen) {
                    this.innerHTML = '<i class="fa-solid fa-eye-slash"></i>';
                } else {
                    this.textContent = "Close Preview";
                }
                preview.classList.remove("d-none");
            }
            else if (preview) {
                if (isMediumScreen) {
                    this.innerHTML = '<i class="fa-solid fa-eye"></i>';
                } else {
                    this.textContent = "Preview";
                }
                preview.classList.add("d-none");
            };

        });
    });
}); */