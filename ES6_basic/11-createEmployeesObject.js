// Write a function named createEmployeesObject that will receive two arguments:
// - departmentName (string)
// - employees (array of strings)
// The function should return an object with the departmentName as a key and the value should be the array of employees.
export default function createEmployeesObject(departmentName, employees) {
    const employee = {
        [departmentName]: employees,
    };

    return employee;
}