

function modalOpen(num, useOrig) {
    (document.getElementById("Modal" + num)).style.display = "block";

    origImgScr = ((document.getElementById("Img" + num)).src).split(".");
    origImgScr.pop();
    if (origImgScr[origImgScr.length - 1].slice(-4) != "_png") {
        (document.getElementById("img" + num)).src = (origImgScr.join(".") + ".jpg");
    }
    else {
        (document.getElementById("img" + num)).src = (origImgScr.join(".") + ".png");
    }
}

function modalClose(num) {
    (document.getElementById("Modal" + num)).style.display = "none";
}



