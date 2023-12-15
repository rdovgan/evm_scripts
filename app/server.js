const express = require('express');
const app = express();
const path = require('path');

app.use(express.static(path.join(__dirname, 'public')));

const port = process.env.PORT || 3000; // Use the provided PORT environment variable or default to 3000

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
