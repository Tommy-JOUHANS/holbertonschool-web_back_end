console.log('Welcome to Holberton School, what is your name?');

process.stdin.setEncoding('utf8');

process.stdin.on('data', (INPUT) => {
  const name = INPUT.trim();
  console.log('Your name is:', name);
  console.log('This important software is now closing');
  process.exit();
});
