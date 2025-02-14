class Calculator {
    add(x, y) {
        return x + y;
    }

    subtract(x, y) {
        return x - y;
    }

    multiply(x, y) {
        return x * y;
    }

    divide(x, y) {
        if (y === 0) {
            throw new Error("Division by zero is not allowed.");
        }
        return x / y;
    }
}

function main() {
    const calculator = new Calculator();
    const readline = require('readline').createInterface({
        input: process.stdin,
        output: process.stdout
    });

    console.log("Welcome to the Calculator!");
    console.log("Options:");
    console.log("1. Add");
    console.log("2. Subtract");
    console.log("3. Multiply");
    console.log("4. Divide");
    console.log("5. Quit");

    readline.question("Enter your choice (1/2/3/4/5): ", choice => {
        if (choice === '5') {
            console.log("Thanks for using the calculator!");
            readline.close();
            return;
        }

        readline.question("Enter the first number: ", num1 => {
            readline.question("Enter the second number: ", num2 => {
                const x = parseFloat(num1);
                const y = parseFloat(num2);

                if (isNaN(x) || isNaN(y)) {
                    console.log("Invalid input. Please enter valid numbers.");
                } else {
                    try {
                        let result;
                        switch (choice) {
                            case '1':
                                result = calculator.add(x, y);
                                console.log(`Result: ${x} + ${y} = ${result}`);
                                break;
                            case '2':
                                result = calculator.subtract(x, y);
                                console.log(`Result: ${x} - ${y} = ${result}`);
                                break;
                            case '3':
                                result = calculator.multiply(x, y);
                                console.log(`Result: ${x} * ${y} = ${result}`);
                                break;
                            case '4':
                                result = calculator.divide(x, y);
                                console.log(`Result: ${x} / ${y} = ${result}`);
                                break;
                            default:
                                console.log("Invalid choice. Please select a valid option.");
                        }
                    } catch (error) {
                        console.log(error.message);
                    }
                }

                readline.close();
            });
        });
    });
}

main();