function calc(n) {
    try {
        var result = eval(n);
        alert(result);
    }
    catch(error) {
        alert("Error!");
    }
}

function getnum() {
    var op = prompt();
    calc(op);
}