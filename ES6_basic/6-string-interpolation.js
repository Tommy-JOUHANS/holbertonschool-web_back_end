export default function getSanFranciscoDescriptions() {
    const year = 2017;
    const budget = {
        income: '$119,868',
        gdp: '$154.2 billion',
        capita: '$178,479',
        
    };

    const str0 = 'As of ';
    const str1 = ', it was the seventh-highest income county in the United States, with a per capita personal income of ';
    const str2 = '.\n As of 2015, San Francisco proper had a GDP of ';
    const str3 = ', and a GDP per capita of ';
    const str4 = '.';

return `${str0}${year}${str1}${budget.income}${str2}${budget.gdp}${str3}${budget.capita}${str4}`;
}