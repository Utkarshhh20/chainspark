import React, { useState } from 'react';
import { Navigate, useNavigate } from 'react-router-dom'; // Import useHistory from react-router-dom
import { GoogleOAuthProvider, GoogleLogin } from '@react-oauth/google';
import './Auth.css';
import logo from '../assets/images/modified-logo-text-transparent.png'; // Import the logo image


const Login = ({ onLogin }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const navigate = useNavigate(); // Initialize the useNavigate hook

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      console.log(`Sending login request for email: ${email}`); // Add log here
      const response = await fetch('http://localhost:5000/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email, password })
      });

      if (response.ok) {
        const data = await response.json();
        alert(data.message);
        if (onLogin) {
          onLogin(data);
        }
        navigate('/home');
      } else {
        const error = await response.text();
        alert(error);
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const handleGoogleLoginSuccess = (response) => {
    console.log(response);
    onLogin();
  };

  const handleGoogleLoginFailure = (response) => {
    console.log(response);
  };

  const handleLogoClick = () => {
    navigate('/'); // Redirect to home page
  };

  return (
    <GoogleOAuthProvider clientId="YOUR_GOOGLE_CLIENT_ID">
      <div className="auth-container">
        <div className="logo-container">
          <img src={logo} alt="ChainSpark" className="logo" onClick={handleLogoClick}/>
        </div>
        <div className="auth-card">
          <h2>Welcome</h2>
          <p>Log in to ChainSpark to access your account</p>
          <form onSubmit={handleLogin}>
            <label>Email</label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="Enter email address"
            />
            <label>Password</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="Enter password"
            />
            <div className="forgot-password">
              <a href="#">Forgot Password?</a>
            </div>
            <button type="submit">Login to your Account</button>
          </form>
          <p>or Sign in with</p>
          <div className="social-login">
            <GoogleLogin
              onSuccess={handleGoogleLoginSuccess}
              onError={handleGoogleLoginFailure}
              useOneTap
            />
          </div>
          <p>
            Don't have an account? <a href="/signup">Register Now</a>
          </p>
        </div>
        <p className="privacy-policy">Privacy policy</p>
      </div>
      <p> ‎  </p>
    </GoogleOAuthProvider>
  );
};

export default Login;
