const cookie = document.querySelector('.cookies')


function removeCookie(){
    cookie.remove()
}

function changeTempFormat(format) {
    var temps = document.querySelectorAll(".tempValue");
    for (var i = 0; i < temps.length; i++) {
        var celsius = Number(temps[i].dataset.celsius);
        if (format === "f") {
            var fahrenheit = Math.round(celsius * 9 / 5 + 32);
            temps[i].innerText = fahrenheit + "°";
        } else {
            temps[i].innerText = celsius + "°";
        }
    }
}