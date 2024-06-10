// src/components/Search.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import PriceChart from './PriceChart';
import Navbar from './Navbar';
import './Search.css';

const Search = () => {
  const [searchQuery, setSearchQuery] = useState('');
  const [results, setResults] = useState([]);
  const [sortOption, setSortOption] = useState('relevance');
  const [filters, setFilters] = useState({
    dateRange: { start: '', end: '' },
    dataType: '',
    priceRange: [0, 100],
    marketCapRange: [0, 1000000000],
  });
  const [currentPage, setCurrentPage] = useState(1);
  const reportsPerPage = 5;

  useEffect(() => {
    fetchReports();
  }, [currentPage]);

  const fetchReports = async () => {
    try {
      const response = await axios.get(`http://localhost:5000/api/reports`, {
        params: {
          page: currentPage,
          pageSize: reportsPerPage,
          searchQuery,
          sortOption,
          ...filters,
        },
      });
      setResults(response.data);
    } catch (err) {
      console.error('Error fetching reports:', err);
    }
  };

  const handleSearch = () => {
    setCurrentPage(1); // Reset to first page on new search
    fetchReports();
  };

  const handleSortChange = (e) => {
    setSortOption(e.target.value);
    setCurrentPage(1); // Reset to first page on sort change
    fetchReports();
  };

  const handleFilterChange = (e) => {
    const { name, value } = e.target;
    setFilters({
      ...filters,
      [name]: value,
    });
    setCurrentPage(1); // Reset to first page on filter change
    fetchReports();
  };

  const indexOfLastReport = currentPage * reportsPerPage;
  const indexOfFirstReport = indexOfLastReport - reportsPerPage;
  const currentReports = results.slice(indexOfFirstReport, indexOfLastReport);

  const paginate = (pageNumber) => setCurrentPage(pageNumber);

  return (
    <div className="search-page">
      <Navbar userName="User Name" sparkTokens="100" />
      <div className="search-bar">
        <input
          type="text"
          placeholder="Search for market data, reports, insights..."
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
        />
        <button onClick={handleSearch}>Search</button>
      </div>
      <div className="sort-options">
        <select value={sortOption} onChange={handleSortChange}>
          <option value="relevance">Relevance</option>
          <option value="date">Date</option>
          <option value="popularity">Popularity</option>
          <option value="price">Price</option>
          <option value="rating">Rating</option>
        </select>
        <button className="advanced-search">Advanced Search</button>
      </div>
      <div className="content">
        <div className="left-sidebar">
          <div className="filters">
            <h3>Filters</h3>
            <div className="filter-group">
              <label>Date Range</label>
              <input type="date" name="startDate" onChange={handleFilterChange} />
              <input type="date" name="endDate" onChange={handleFilterChange} />
            </div>
            <div className="filter-group">
              <label>Data Type</label>
              <select name="dataType" onChange={handleFilterChange}>
                <option value="">All</option>
                <option value="reports">Reports</option>
                <option value="datasets">Datasets</option>
                <option value="analysis">Analysis</option>
              </select>
            </div>
            <div className="filter-group">
              <label>Price Range</label>
              <input type="range" name="priceRange" min="0" max="100" value={filters.priceRange} onChange={handleFilterChange} />
              <p>1 - 100</p>
            </div>
            <div className="filter-group">
              <label>Market Cap Range (in millions)</label>
              <input type="range" name="marketCapRange" min="0" max="1000000" value={filters.marketCapRange} onChange={handleFilterChange} />
            </div>
          </div>
        </div>
        <div className="main-content">
          <div className="search-results">
            {currentReports.map((item, index) => (
              <div className="search-item" key={index}>
                <div className="chart-container">
                <PriceChart symbol={item.symbol} />
                </div>
                <div className="item-details">
                  <h2>{item.reportName}</h2>
                  <h4>{item.cryptoName}</h4>
                  <p>Price: {item.price}</p>
                  <p>Rating: {item.rating}</p>
                  <p>Date: {item.datePublished}</p>
                  <p>User: {item.user}</p>
                  <button className="buy-button">Buy</button>
                </div>
              </div>
            ))}
          <div className="pagination">
            {Array.from({ length: Math.ceil(results.length / reportsPerPage) }, (_, i) => (
              <button key={i} onClick={() => paginate(i + 1)}>
                {i + 1}
              </button>
            ))}
          </div>
          </div>
        </div>
        <div className="right-sidebar">
          <div className="recently-viewed">
            <h3>Recently Viewed</h3>
          </div>
          <div className="recommended">
            <h3>Recommended</h3>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Search;
