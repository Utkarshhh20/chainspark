// src/components/PriceChart.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';

const PriceChart = ({ symbol }) => {
  const [data, setData] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(`http://localhost:5000/api/historical-data/${symbol}`);
        setData(response.data);
      } catch (err) {
        console.error('Error fetching data:', err);
        setError('Error fetching data');
      }
    };

    fetchData();
  }, [symbol]);

  if (error) {
    return <div>{error}</div>;
  }

  return (
    <LineChart width={550} height={400} data={data}>
      <CartesianGrid strokeDasharray="3 3" />
      <XAxis dataKey="date" />
      <YAxis />
      <Tooltip />
      <Legend />
      <Line type="monotone" dataKey="close" stroke="#8884d8" dot={false} />
    </LineChart>
  );
};

export default PriceChart;