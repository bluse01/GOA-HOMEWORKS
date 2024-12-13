function Check_String(str) {
    const noneAlpha = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "?"];

    for(let i = 0; i < str.length; i++) {
        for(let j = 0; j < noneAlpha.length; j++) {
            if(str[i] == noneAlpha[j]) {
                return "Error String contains number/symbols!";
            }
        }
    }

    return "Clean String!";
}

alert(Check_String(prompt("str: ")));