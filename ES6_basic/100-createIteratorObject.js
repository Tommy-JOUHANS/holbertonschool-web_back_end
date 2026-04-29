export default function createIteratorObject(report) {
  const employees = report.allEmployees;
  const departments = Object.keys(employees);
  let index = 0;
  let departmentIndex = 0;

  return {
    [Symbol.iterator]() { return this; },   // ← ajoute ceci
    next() {
      if (departmentIndex >= departments.length) {
        return { value: undefined, done: true };
      }
      const department = departments[departmentIndex];
      const employee = employees[department][index];
      index++;
      if (index >= employees[department].length) {
        index = 0;
        departmentIndex++;
      }
      return { value: employee, done: false };
    },
  };
}