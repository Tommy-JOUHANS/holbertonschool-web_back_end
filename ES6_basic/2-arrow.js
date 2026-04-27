export default function getNeighborhoodsList() {
    this.neighborhoods = ['SOMA', 'Union Square'];
    this.addNeighborhood = function (neighborhood) {
        this.neighborhoods.push(neighborhood);
        return this.neighborhoods;
    };
}