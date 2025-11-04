function colour_change(speed) {
    let r = 0;
    let g = 0;
    let b = 0;
    let changeElement = document.querySelector("#stretch");
    let count = 0;

    let intervalId = setInterval(() => {
        console.log(r, g, b);
        changeElement.style.backgroundColor = `rgb(${r},${g},${b})`;
        r++;
        if (r == 256) {
            g++;
            while (r !== 0){
                r--
                changeElement.style.backgroundColor = `rgb(${r},${g},${b})`;
            }
        }
        if (g == 256) {
            b++;
            while (g !== 0){
                g--
                changeElement.style.backgroundColor = `rgb(${r},${g},${b})`;
            }
        }
        if (b == 256) {

            while (r !== 255 && g !== 255 && b !== 255){
                while (r !== 255){
                    r++
                    changeElement.style.backgroundColor = `rgb(${r},${g},${b})`;
                }
                while (g !== 255){
                    g--
                    changeElement.style.backgroundColor = `rgb(${r},${g},${b})`;
                }
                while (b !== 255){
                    b--
                    changeElement.style.backgroundColor = `rgb(${r},${g},${b})`;
                }
            }

            while (r != -1) {
                changeElement.style.backgroundColor = `rgb(${r},${g},${b})`;
                b--;
                if (b == -1) {
                    g--;
                    b = 255;
                }
                if (g == -1) {
                    r--;
                    g = 255;
                }
            }
            b = 0;
            g = 0;
            r = 0;
        }

        count++;

        if (count > Math.random() * 250 + 33162750) {
            clearInterval(intervalId);
        }
    }, speed);
    let button_colourid = document.querySelector("#warning")
    button_colourid.innerHTML = `<input type="button" id = "button_colour" value="the button is deactivated now" >`
}

colour_change(1000);
function flash(speed){
    let button_colourid = document.querySelector("#warning")
    button_colourid.innerHTML = `<input type="button" id = "button_colour" value="I WARNED YOU" onclick="flash(1)">`
    setTimeout(() => {
        let count = 0
        let flash_interval = setInterval(() => {
            colour_change(speed)
            count++
            if (count >= 33162750){
                clearInterval(flash_interval);
            }
        },1)
    },5000)
}