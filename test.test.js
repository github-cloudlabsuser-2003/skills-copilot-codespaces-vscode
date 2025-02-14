const { expect } = require('chai');
const Calculator = require('./test.js');

// filepath: /workspaces/skills-copilot-codespaces-vscode/test.test.js

describe('Calculator', () => {
    let calculator;

    beforeEach(() => {
        calculator = new Calculator();
    });

    describe('add', () => {
        it('should return the sum of two numbers', () => {
            expect(calculator.add(2, 3)).to.equal(5);
        });

        it('should return a negative number when adding a positive and a negative number', () => {
            expect(calculator.add(2, -3)).to.equal(-1);
        });

        it('should return zero when adding zero to a number', () => {
            expect(calculator.add(2, 0)).to.equal(2);
        });
    });

    describe('subtract', () => {
        it('should return the difference of two numbers', () => {
            expect(calculator.subtract(5, 3)).to.equal(2);
        });

        it('should return a negative number when the second number is larger', () => {
            expect(calculator.subtract(2, 3)).to.equal(-1);
        });

        it('should return the same number when subtracting zero', () => {
            expect(calculator.subtract(2, 0)).to.equal(2);
        });
    });

    describe('multiply', () => {
        it('should return the product of two numbers', () => {
            expect(calculator.multiply(2, 3)).to.equal(6);
        });

        it('should return zero when multiplying by zero', () => {
            expect(calculator.multiply(2, 0)).to.equal(0);
        });

        it('should return a negative number when multiplying a positive and a negative number', () => {
            expect(calculator.multiply(2, -3)).to.equal(-6);
        });
    });

    describe('divide', () => {
        it('should return the quotient of two numbers', () => {
            expect(calculator.divide(6, 3)).to.equal(2);
        });

        it('should throw an error when dividing by zero', () => {
            expect(() => calculator.divide(6, 0)).to.throw("Division by zero is not allowed.");
        });

        it('should return a negative number when dividing a positive and a negative number', () => {
            expect(calculator.divide(6, -3)).to.equal(-2);
        });
    });
});