const bt = document.getElementById("button");
const hero = document.getElementById("hero_text");

function change_text() {
    if(hero.innerHTML == "Hello") {
        hero.innerHTML = "GoodBye"
    }
    else {
        hero.innerHTML = "Hello"
    }
}