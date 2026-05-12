const http = require('http');

const p = 1245;

const list = function listener(request, response) {
  response.statusCode = 200;
  response.setHeader('Content-Type', 'text/plain');
  response.end('Hello Holberton School!');
};

const app = http.createServer(list);

app.listen(p);

module.exports = app;
