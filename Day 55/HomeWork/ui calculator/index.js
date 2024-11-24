var display = document.getElementById("display");

function input(key) {
    display.value += key;
}

function clearall() {
    display.value = "";
}

function backspace() {
    display.value = display.value.slice(0, -1)
}

function calc() {
    try {
        display.value = eval(display.value);
    }
    catch(error) {
        display.value = "Error";
    }
}