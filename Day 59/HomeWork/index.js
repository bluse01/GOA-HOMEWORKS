function remove_spaces(str) {
    let result_string = "";
    for(let i = 0; i < str.length; i++) {
        if(str[i] != ' ') {
            result_string += str[i];
        }
    }

    return result_string;
}

function handleSubmit() {
    const form_inputs = document.querySelectorAll('input[type="text"]');

    if (document.getElementById("checkbox").checked) {
        for(let i = 0; i < form_inputs.length; i++) {
            let vl_str = remove_spaces(form_inputs[i].value);
            if(vl_str) {
                alert(form_inputs[i].value);
            }
            else {
                alert("empty");
            }
        }
    } else {
        alert("Check is not cheked!");
    }
}
