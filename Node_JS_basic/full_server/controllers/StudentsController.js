import { readDatabase } from '../utils';

export default class StudentsController {
  static getAllStudents(request, response) {
    try {
      const data = readDatabase();
      let output = 'This is the list of our students\n';
      const fields = Object.keys(data).sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));
      for (const field of fields) {
        const students = data[field];
        const firstNames = students.map(s => s.firstName);
        output += `Number of students in ${field}: ${students.length}. List: ${firstNames.join(', ')}\n`;
      }
      response.status(200).send(output);
    } catch (error) {
      response.status(500).send('Cannot load the database');
    }
  }

  static getAllStudentsByMajor(request, response) {
    const major = request.params.major;
    if (major !== 'CS' && major !== 'SWE') {
      response.status(500).send('Major parameter must be CS or SWE');
      return;
    }
    try {
      const data = readDatabase();
      const students = data[major];
      const firstNames = students.map(s => s.firstName);
      const output = `List: ${firstNames.join(', ')}`;
      response.status(200).send(output);
    } catch (error) {
      response.status(500).send('Cannot load the database');
    }
  }
}