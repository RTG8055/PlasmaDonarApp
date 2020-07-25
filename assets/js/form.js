function changeForm(toLang){
    var eng = document.getElementById("toggle-english");
    eng.style.display = "none";
    var hin = document.getElementById("toggle-hindi");
    hin.style.display = "none";
    var tel = document.getElementById("toggle-telugu");
    tel.style.display = "none";

    var x= document.getElementById("toggle-"+toLang);
    x.style.display = "block";
}