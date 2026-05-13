import express from 'express';
import router from './routes/index.js';

const app = express();

const databaseFile = process.argv[2];

app.use('/', router(databaseFile));

const PORT = 1245;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

export default app;
