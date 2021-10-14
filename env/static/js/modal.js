u7// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function () {
    modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function () {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
// CALCULATOR

var entries = [];
var total = 0;

var temp = '';
$("button").on('click', function () {
    var val = $(this).text();

    // Got a number, add to temp
    if (!isNaN(val) || val === '.') {
        temp += val;
        $("#answer").val(temp.substring(0, 10));

        // Got some symbol other than equals, add temp to our entries
        // then add our current symbol and clear temp
    } else if (val === 'AC') {
        entries = [];
        temp = '';
        total = 0;
        $("#answer").val('')

        // Clear last entry
    } else if (val === 'CE') {
        temp = '';
        $("#answer").val('')

        // Change multiply symbol to work with eval
    } else if (val === 'x') {
        entries.push(temp);
        entries.push('*');
        temp = '';

        // Change divide symbol to work with eval
    } else if (val === '÷') {
        entries.push(temp);
        entries.push('/');
        temp = '';

        // Got the equals sign, perform calculation
    } else if (val === '=') {
        entries.push(temp);

        var nt = Number(entries[0]);
        for (var i = 1; i < entries.length; i++) {
            var nextNum = Number(entries[i + 1])
            var symbol = entries[i];

            if (symbol === '+') { nt += nextNum; }
            else if (symbol === '-') { nt -= nextNum; }
            else if (symbol === '*') { nt *= nextNum; }
            else if (symbol === '/') { nt /= nextNum; }

            i++;
        }

        // Swap the '-' symbol so text input handles it correctly
        if (nt < 0) {
            nt = Math.abs(nt) + '-';
        }

        $("#answer").val(nt);
        entries = [];
        temp = '';

        // Push number
    } else {
        entries.push(temp);
        entries.push(val);
        temp = '';
    }
});