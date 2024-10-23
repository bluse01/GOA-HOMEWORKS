function operations(num1, num2) {
    const opList = [
        (a, b) => a + b,
        (a, b) => a - b,
        (a, b) => a * b,
        (a, b) => a / b
    ];

    opList.forEach(op => {
        console.log(op(num1, num2));
    });
}

const num1 = 5;
const num2 = 7;

operations(num1, num2);