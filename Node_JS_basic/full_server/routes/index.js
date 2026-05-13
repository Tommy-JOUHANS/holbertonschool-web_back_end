const express = require('express');
const router = express.Router();

const AppController = require('../controllers/AppController');
const StudentsController = require('../controllers/StudentsController');

router.use('/', AppController);
router.use('/students', StudentsController);

module.exports = router;
