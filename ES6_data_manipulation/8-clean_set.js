export default function cleanSet(set, startString) {
   if (startString === '') {
    return '';
  }

    if (!(set instanceof Set) || typeof startString !== 'string') {
    return '';
  }
    const result = [];
    for (const item of set) {
        if (item.startsWith(startString)) {
            result.push(item.slice(startString.length));
        }
    }
    return result.join('-');
}