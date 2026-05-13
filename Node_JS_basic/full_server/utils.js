const fs = require('fs').promises;

async function readDatabase(filePath) {
  const data = await fs.readFile(filePath, 'utf-8');
  const lines = data.trim().split('\n');
  const result = {};

  if (lines.length <= 1) {
    return result;
  }

  const headers = lines[0].split(',');
  const firstNameIndex = headers.indexOf('firstname');
  const fieldIndex = headers.indexOf('field');

  for (const line of lines.slice(1)) {
    if (!line.trim()) continue;
    const values = line.split(',');
    if (values.length !== headers.length) continue;

    const firstName = values[firstNameIndex].trim();
    const field = values[fieldIndex].trim();

    if (!field || !firstName) continue;
    if (!result[field]) {
      result[field] = [];
    }
    result[field].push(firstName);
  }

  return result;
}

module.exports = readDatabase;
