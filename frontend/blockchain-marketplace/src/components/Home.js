import React, { useRef } from 'react';
import './Home.css';
import { Navigate, useNavigate } from 'react-router-dom'; // Import useHistory from react-router-dom
import logo from '../assets/images/modified-logo-text-transparent.png'; // Import the logo image

const Home = () => {

  const navigate = useNavigate(); // Initialize the useNavigate hook

  const handleLogoClick = () => {
    navigate('/search'); // Redirect to home page
  };

  return (
    <div>
      <h2>Welcome to the Blockchain Marketplace</h2>
      <p>Browse and upload financial reports securely.</p>
      <div className="logo-container">
          <img src={logo} alt="ChainSpark" className="logo" onClick={handleLogoClick}/>
        </div>
    </div>
  );
};

export default Home;