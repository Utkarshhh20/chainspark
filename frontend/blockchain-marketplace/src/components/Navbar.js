import logo from '../assets/images/modified-logo-text-transparent.png'; // Import the logo image
import sparktoken_img from '../assets/images/sparkcoin.png'; // Import the logo image
import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';

const Navbar = ({ userName, sparkTokens }) => {
  return (
    <div className="navbar">
      <div className="logo">
        <img src={logo} alt="Chain Spark" />
      </div>
      <div className="nav-links">
        <Link to="/">Home</Link>
        <span className="separator">|</span>
        <Link to="/upload">Upload</Link>
        <span className="separator">|</span>
        <Link to="/search">Search</Link>
        <span className="separator">|</span>
        <div className="spark-tokens">{sparkTokens} ‎ <img src={sparktoken_img} alt="SparkToken" className="sparktoken"></img> </div>
        <div className="user-menu">
          {userName} 👤
          <div className="dropdown">
            <Link to="/settings">Settings</Link>
            <Link to="/logout">Logout</Link>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Navbar;
