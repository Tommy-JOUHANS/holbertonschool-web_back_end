import Currency from "./3-currency.js";

export default class Pricing {
    constructor(amount, currency) {
        this._amount = amount;
        this._currency = currency;
    }

    get amount() {
        return this._amount;
    }

    set amount(newAmount) {
        if (typeof newAmount !== 'number') {
            throw new TypeError('Amount must be a number');
        }
        this._amount = newAmount;
    }

    get currency() {
        return this._currency;
    }

    set currency(newCurrency) {
        if (!(newCurrency instanceof Currency)) {
            throw new TypeError('Currency must be an instance of Currency');
        }
        this._currency = newCurrency;
    }

    displayFullPrice() {
        return `${this._amount} ${this._currency.displayFullCurrency()}`;
    }

    static convertPrice(amount, conversionRate) {
        if (typeof amount !== 'number') {
            throw new TypeError('Amount must be a number');
        }
        if (typeof conversionRate !== 'number') {
            throw new TypeError('Conversion rate must be a number');
        }
        return amount * conversionRate;
    }

    static conversionRate(fromCurrency, toCurrency) {
        if (!(fromCurrency instanceof Currency) || !(toCurrency instanceof Currency)) {
            throw new TypeError('Both parameters must be instances of Currency');
        }
        const rates = {
            'USD': 1,
            'EUR': 0.85,
            'GBP': 0.75,
            'JPY': 110,
        };
        const fromRate = rates[fromCurrency.code];
        const toRate = rates[toCurrency.code];
        if (fromRate === undefined || toRate === undefined) {
            throw new Error('Unsupported currency code');
        }
        return toRate / fromRate;
    }
}
