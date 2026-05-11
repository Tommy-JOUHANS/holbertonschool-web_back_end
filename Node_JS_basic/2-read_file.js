const fs = require('fs');

module.exports = function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.split('\n');

    const students = lines.slice(1).filter((line) => line.trim().length > 0);

    console.log(`Number of students: ${students.length}`);

    const fields = {};
    students.forEach((line) => {
      const [firstname, , , field] = line.split(',');
      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(firstname);
    });

    for (const field in fields) {
      if (Object.prototype.hasOwnProperty.call(fields, field)) {
        const count = fields[field].length;
        const names = fields[field].join(', ');
        console.log(`Number of students in ${field}: ${count}. List: ${names}`);
      }
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
};
