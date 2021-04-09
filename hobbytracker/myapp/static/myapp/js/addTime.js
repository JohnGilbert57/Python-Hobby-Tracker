// File Created: Johnny Gilbert, Nathaniel Buchanan, Nathan Bennett
// Ohio University

var submitButtons = document.querySelectorAll('[submit-button]');

// Checking if the values are accurate for each day of the week
// to submit to the database
submitButtons.forEach(button => {
    button.addEventListener('click', () => {
        var a = document.getElementById("id_sunTime").value;
        var b = document.getElementById("id_monTime").value;
        var c = document.getElementById("id_tueTime").value;
        var d = document.getElementById("id_wedTime").value;
        var e = document.getElementById("id_thuTime").value;
        var f = document.getElementById("id_friTime").value;
        var g = document.getElementById("id_satTime").value;
        if(a <= 24 && a >= 0 && b <= 24 && b >= 0
            && c <= 24 && c >= 0 && d <= 24 && d >= 0
            && e <= 24 && e >= 0 && f <= 24 && f >= 0
            && g <= 24 && g >= 0){
            document.getElementById("forms").submit();
        }
    })
})