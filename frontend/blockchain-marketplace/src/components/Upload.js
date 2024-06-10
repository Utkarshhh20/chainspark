import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Papa from 'papaparse';
import Select from 'react-select';
import Navbar from './Navbar';
import { Worker, Viewer } from '@react-pdf-viewer/core';
import '@react-pdf-viewer/core/lib/styles/index.css';
import './Upload.css';

const UploadPage = () => {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [price, setPrice] = useState('');
  const [ticker, setTicker] = useState(null);
  const [tickers, setTickers] = useState([]);
  const [file, setFile] = useState(null);
  const [fileUrl, setFileUrl] = useState(null);
  const [error, setError] = useState('');

  // Load the CSV file and parse it
  useEffect(() => {
    const fetchTickers = async () => {
      try {
        const response = await axios.get('/crypto_tickers.csv'); // Fetching the CSV from public folder
        Papa.parse(response.data, {
          header: true,
          skipEmptyLines: true,
          complete: (result) => {
            const tickerOptions = result.data.map(t => ({
              value: t['currency code'],
              label: t['currency name']
            }));
            setTickers(tickerOptions);
          }
        });
      } catch (error) {
        console.error('Error fetching tickers:', error);
      }
    };

    fetchTickers();
  }, []);
  
  const preDeterminedPdfUrl = '/Ethereum Investment Analysis 2024-05-21.pdf'; // Relative path to your PDF file in the public folder

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    setFile(selectedFile);
    setFileUrl(URL.createObjectURL(selectedFile));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!title || !description || !price || !ticker) {
      setError('All fields are required');
      return;
    }
    if (ticker.value !== 'N/A' && !tickers.find(t => t.value === ticker.value)) {
      setError('Invalid ticker symbol');
      return;
    }

    // Add your submit logic here
    console.log('Form submitted:', { title, description, price, ticker: ticker.value });
  };

  const handleTickerChange = (selectedOption) => {
    setTicker(selectedOption);
  };

  const customStyles = {
    control: (provided) => ({
      ...provided,
      color: 'black',
    }),
    singleValue: (provided) => ({
      ...provided,
      color: 'black',
    }),
    option: (provided, state) => ({
      ...provided,
      color: 'black',
      backgroundColor: state.isFocused ? 'lightgrey' : 'white',
    }),
  };

  return (
    <div className="upload-page">
      <Navbar userName="User Name" sparkTokens="100" />
      <h1 className="upload-header">Upload New Report</h1>
      <div className="upload-content">
        <form className="upload-form" onSubmit={handleSubmit}>
          <input
            className="report-details"
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            placeholder="Title of your report"
          />
          <textarea
            className="report-details"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            placeholder=" Description of your report"
          />
          <input
            className="report-details"
            type="number"
            value={price}
            onChange={(e) => setPrice(e.target.value)}
            placeholder="Price"
          />
          <Select
          className="category-select"
            value={ticker}
            onChange={handleTickerChange}
            options={[{ value: 'N/A', label: 'N/A' }, ...tickers]}
            styles={customStyles}
            placeholder="Crypto Ticker (if not applicable, enter N/A)"
          />
          {error && <p className="error">{error}</p>}
          <div className="file-upload">
            <input type="file" onChange={handleFileChange} required />
          </div>
          <button type="submit">Upload your report</button>
          <div className="tips-section">
        <h2>Tips for Creating a High-Quality Report</h2>
          <ul>
            <li>Use clear and concise language.</li>
            <li>Include graphs and visualizations to support your data.</li>
            <li>Ensure your report is well-structured with appropriate headings.</li>
            <li>Provide detailed descriptions and analyses.</li>
            <li>Use keywords such as 'Analysis', 'Dataset', 'Market Data', etc.</li>
          </ul>
      </div>
        </form>
        <div className="example-report">
        <h2>Example Report</h2>
            <div className="pdf-viewer">
              <Worker workerUrl={`https://unpkg.com/pdfjs-dist@3.0.279/build/pdf.worker.min.js`}>
                <Viewer fileUrl={preDeterminedPdfUrl} />
              </Worker>
            </div>
          {error && <p className="error">{error}</p>}
        </div>
        </div>
    </div>
  );
};

export default UploadPage;
