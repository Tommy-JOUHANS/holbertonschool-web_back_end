function getBudgetForCurrentYear() {

    const date = new Date();
    return date.getFullYear();
}

export default function getBudgetForCurrentYear(income, gdp, capita) {
    const budget = {income, gdp, capita};
    const currentYear = getBudgetForCurrentYear();
    return `As of ${currentYear}, the budget is: ${JSON.stringify(budget)}`;
}
