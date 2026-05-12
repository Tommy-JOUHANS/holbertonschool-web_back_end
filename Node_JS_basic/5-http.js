const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer((request, response) => {
  response.statusCode = 200;
  response.setHeader('Content-Type', 'text/plain');

  if (request.url === '/') {
    response.end('Hello Holberton School!');
  } else if (request.url === '/students') {
    const database = process.argv[2];
    countStudents(database)
      .then((output) => {
        response.end(`This is the list of our students\n${output}`);
      })
      .catch(() => {
        response.end('This is the list of our students\nCannot load the database');
      });
  } else {
    response.end();
  }
});

app.listen(1245);

module.exports = app;
