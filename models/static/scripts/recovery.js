document.addEventListener('DOMContentLoaded', function () {
    const bankButton = document.getElementById('bankButton');
    const cryptoButton = document.getElementById('cryptoButton');
    const cashButton = document.getElementById('cashButton');

    const bankSection = document.getElementById('bankSection');
    const cryptoSection = document.getElementById('cryptoSection');
    const cashSection = document.getElementById('cashSection');

    bankButton.addEventListener('click', function () {
        bankSection.classList.remove('hidden');
        cryptoSection.classList.add('hidden');
        cashSection.classList.add('hidden');
    });

    cryptoButton.addEventListener('click', function () {
        bankSection.classList.add('hidden');
        cryptoSection.classList.remove('hidden');
        cashSection.classList.add('hidden');
    });

    cashButton.addEventListener('click', function () {
        bankSection.classList.add('hidden');
        cryptoSection.classList.add('hidden');
        cashSection.classList.remove('hidden');
    });
});

