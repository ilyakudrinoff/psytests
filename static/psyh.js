function be_continued() {
    var soglasie = document.getElementById("soglasie");
    var konf = document.getElementById("konf");
    var button = document.getElementById("button_continue");

    if (soglasie.checked & konf.checked) {
        button.disabled = false;
    }
    else {
        button.disabled = true;
    }
}