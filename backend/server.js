const express = require('express');
const mysql = require('mysql2');
const cors = require('cors');
const axios = require('axios'); // Ensure axios is imported

const app = express();
const port = process.env.PORT || 5000;


app.use(cors());
app.use(express.json());

// MySQL database connection
const db = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'ENTER_YOUR_PASS',
  database: 'chainspark'
});

db.connect(err => {
  if (err) {
    console.error('Error connecting to the database:', err);
    return;
  }
  console.log('Connected to the database');
});

// Default route for debugging
app.get('/', (req, res) => {
  res.send('Backend server is running');
});

// Endpoint to fetch historical data from Alpha Vantage
app.get('/api/historical-data/:symbol', async (req, res) => {
  const symbol = req.params.symbol;
  const API_KEY = 'ALPHAVANTAGE_API' 
  try {
    const response = await axios.get(`https://www.alphavantage.co/query`, {
      params: {
        function: 'DIGITAL_CURRENCY_DAILY',
        symbol: symbol,
        market: 'USD',
       // outputsize: 'compact',
        apikey: API_KEY,
      },
    });

    const timeSeries = response.data['Time Series (Digital Currency Daily)'];
    if (!timeSeries) {
      throw new Error('Time Series data not available');
    }

    const chartData = Object.keys(timeSeries).map(date => ({
      date,
      close: parseFloat(timeSeries[date]['4. close']),
    })).reverse();

    res.json(chartData);
  } catch (err) {
    console.error('Error fetching data:', err);
    res.status(500).json({ error: 'Error fetching data' });
  }
});

// Login endpoint
app.post('/login', (req, res) => {
  const { email, password } = req.body;
  console.log(`Received login request for email: ${email}`);
  console.log(`Password provided: ${password}`);

  db.query('SELECT * FROM login WHERE email = ? AND password_hash = ?', [email, password], (err, results) => {
    if (err) {
      console.error('Database query error:', err);
      return res.status(500).send('Server error');
    }

    if (results.length === 0) {
      console.log('Invalid email or password');
      return res.status(401).send('Invalid email or password');
    }

    console.log('Login successful');
    res.json({ message: 'Login successful', user: results[0] });
  });
});

// Signup endpoint
app.post('/signup', (req, res) => {
  const { first_name, last_name, email, password, confirm_password, dob } = req.body;
  console.log(`Received signup request for email: ${email}`);

  // Check for empty fields
  if (!first_name || !last_name || !email || !password || !confirm_password || !dob) {
    return res.status(400).send('All fields are required');
  }

  // Check if passwords match
  if (password !== confirm_password) {
    return res.status(400).send('Passwords do not match');
  }

  // Check if email is unique
  db.query('SELECT * FROM login WHERE email = ?', [email], (err, results) => {
    if (err) {
      console.error('Database query error:', err);
      return res.status(500).send('Server error');
    }

    if (results.length > 0) {
      return res.status(400).send('Email already exists');
    }

    // Insert the new user into the database
    db.query('INSERT INTO login (first_name, last_name, email, password_hash, dob) VALUES (?, ?, ?, ?, ?)', [first_name, last_name, email, password, dob], (err, results) => {
      if (err) {
        console.error('Database insertion error:', err);
        return res.status(500).send('Server error');
      }

      console.log('Signup successful');
      res.json({ message: 'Signup successful' });
    });
  });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
