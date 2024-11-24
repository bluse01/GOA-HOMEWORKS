document.getElementById("m-button").addEventListener("click", function(e) {
    e.preventDefault();

    const name = document.getElementById("name-input").value;
    const last_name = document.getElementById("lastname-input").value;
    const user_age = document.getElementById("age-input").value;

    const new_div = document.createElement("div");
    if(user_age >= 18) {
        new_div.innerHTML = `
        <p>Welcome ${name} ${last_name}, your age is ${user_age}</p>
        <p>You're over 18 you can use this site!<p>
        `;   
    }
    else{
        new_div.innerHTML = `
        <p>Welcome ${name} ${last_name}, your age is ${user_age}</p>
        <p>You're under 18 you can't use this site<p>
        `;   
    }

    document.getElementById("container").appendChild(new_div);
});