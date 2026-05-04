export default function hasValuesFromArray(set, array) {
  if (!(set instanceof Set) || !Array.isArray(array)) {
    return false;
  }

  for (const value of array) {
    if (!set.has(value)) {
      return false;
    }
  }

  return true;
}