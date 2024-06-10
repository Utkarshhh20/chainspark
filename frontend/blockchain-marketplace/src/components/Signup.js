import React, { useState } from 'react';
import { Navigate, useNavigate } from 'react-router-dom'; // Import useHistory from react-router-dom
import { GoogleOAuthProvider, GoogleLogin } from '@react-oauth/google';
import './Auth.css';
import logo from '../assets/images/modified-logo-text-transparent.png'; // Import the logo image

const Signup = ({ onSignup }) => {
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [dob, setDob] = useState('');
  const navigate = useNavigate();

  const handleSignup = async (e) => {
    e.preventDefault();

    // Check for empty fields
    if (!firstName || !lastName || !email || !password || !confirmPassword || !dob) {
      alert('All fields are required');
      return;
    }

    // Check if passwords match
    if (password !== confirmPassword) {
      alert('Passwords do not match');
      return;
    }

    // Check if user is at least 16 years old
    const age = new Date().getFullYear() - new Date(dob).getFullYear();
    if (age < 16) {
      alert('You must be at least 16 years old');
      return;
    }

    try {
      console.log(`Sending signup request for email: ${email}`);
      const response = await fetch('http://localhost:5000/signup', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ first_name: firstName, last_name: lastName, email, password, confirm_password: confirmPassword, dob })
      });

      if (response.ok) {
        const data = await response.json();
        alert(data.message);
        if (onSignup) {
          onSignup(data.user);
        }
        navigate('/login');
      } else {
        const error = await response.text();
        alert(error);
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const handleGoogleSignupSuccess = (response) => {
    console.log(response);
    onSignup();
  };

  const handleGoogleSignupFailure = (response) => {
    console.log(response);
  };

  return (
    <GoogleOAuthProvider clientId="YOUR_GOOGLE_CLIENT_ID">
      <div className="auth-container">
        <p> ‎  </p>
        <div className="auth-card">
          <h2>Create Your ChainSpark Account</h2>
          <p>Get started for free by signing up now.</p>
          <form onSubmit={handleSignup}>
            <div className="name-fields">
              <div className="name-field">
                <label>First Name</label>
                <input
                  type="text"
                  value={firstName}
                  onChange={(e) => setFirstName(e.target.value)}
                  placeholder="Enter first name"
                />
              </div>
              <div className="name-field">
                <label>Last Name</label>
                <input
                  type="text"
                  value={lastName}
                  onChange={(e) => setLastName(e.target.value)}
                  placeholder="Enter last name"
                />
              </div>
            </div>
            <div className="info-fields">
              <div className="info-field">
                <label>Email</label>
                <input
                  type="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  placeholder="Enter email address"
                />
              </div>
              <div className="info-field">
                <label>Date of Birth</label>
                <input
                  type="date"
                  value={dob}
                  onChange={(e) => setDob(e.target.value)}
                />
              </div>
            </div>
            <label>Password</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="Enter password"
            />
            <label>Confirm Password</label>
            <input
              type="password"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              placeholder="Confirm password"
            />
            <button type="submit">Create your Account</button>
          </form>
          <p>or Sign up with</p>
          <div className="social-login">
            <GoogleLogin
              onSuccess={handleGoogleSignupSuccess}
              onError={handleGoogleSignupFailure}
              useOneTap
            />
          </div>
          <p>
            Already have an account? <a href="/login">Login Now</a>
          </p>
        </div>
        <p className="privacy-policy">Privacy policy</p>
      </div>
      <p> ‎  </p>
    </GoogleOAuthProvider>
  );
};

export default Signup;
