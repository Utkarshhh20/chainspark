import React, { useRef } from 'react';
import './LandingPage.css';
import logo from '../assets/images/modified-logo-text-transparent.png'; // Import the logo image
import backgroundImage from '../assets/images/black_bg.jpg'; // Import the background image 
import trading_illustration from '../assets/images/trading-illustration.png';
import cash from '../assets/images/money.png';
import home_img from '../assets/images/home-img.png';
import benefits_1 from '../assets/images/benefits-1.png'; 
import benefits_2 from '../assets/images/benefits-2.png';
import filler_img from '../assets/images/landingpage-bg.png';
import linkedinLogo from '../assets/images/linkedin-logo2.png';
import githubLogo from '../assets/images/github-logo2.png';
import card_img1 from '../assets/images/card1.png';
import card_img2 from '../assets/images/card2.png';
import card_img3 from '../assets/images/card3.png';
import card_img4 from '../assets/images/card4.png';
import contact_img from '../assets/images/contact-img.png';


const LandingPage = () => {
  const topRef = useRef(null);
  const homeRef = useRef(null);
  const aboutRef = useRef(null);
  const servicesRef = useRef(null);
  const teamRef = useRef(null);
  const newsRef = useRef(null);

  const scrollToRef = (ref) => {
    window.scrollTo({
      top: ref.current.offsetTop - window.innerHeight / 2 + ref.current.clientHeight / 2,
      behavior: 'smooth',
    });
  };

  return (
    <div className="landing-container" style={{ backgroundImage: `url(${backgroundImage})` }}>
      <header className="landing-header">
        <img src={logo} alt="ChainSpark" className="landing-logo" onClick={() => scrollToRef(topRef)} />
        <nav className="landing-nav">
          <a href="#home" onClick={() => scrollToRef(homeRef)}>Home</a>
          <a href="#about" onClick={() => scrollToRef(aboutRef)}>About</a>
          <a href="#services" onClick={() => scrollToRef(servicesRef)}>Services</a>
          <a href="#team" onClick={() => scrollToRef(teamRef)}>Team</a>
          <a href="#contact" onClick={() => scrollToRef(newsRef)}>News</a>
          <a href="/login" className="login-button">Log In</a>
        </nav>
      </header>
      <main className="landing-main">
        <div className="main-content" ref={topRef}>
          <div className="text-content">
            <h1>
              Decentralized Financial Reports Marketplace.
              <img src={cash} alt="Cash Icon" className="cash-img" />
            </h1>
            <p className="more-text">Redefining Financial Insights with Blockchain.</p>
            <div className="landing-buttons">
              <a href="/login" className="landing-button">Login</a>
              <a href="/signup" className="landing-button">Sign Up</a>
            </div>
          </div>
          <div className="image-content">
            <img src={trading_illustration} alt="Trading Illustration" className="main-img" />
          </div>
        </div>
        <div className="continuation-content" ref={homeRef}>
          <div className="defined-section">
            <div className="defined-image">
              <img src={home_img} alt="Blockchain Image" />
            </div>
            <div className="defined-text">
              <h2>CHAINSPARK</h2>
              <p>
                ChainSpark is your gateway to decentralized financial insights. With our platform, you can access or sell a wide range of financial reports and data it while it all being securely stored and verified on the blockchain. Our AI-driven analysis provides you with actionable insights, helping you make informed investment decisions.
              </p>
              <a href="#read-more" className="read-more-button">Read More</a>
            </div>
          </div>
        </div>
        <section className="benefits" ref={aboutRef}>
          <div className="benefit-heading">
          </div>
          <div className="benefit-boxes">
            <div className="benefit-box">
              <h3>Investment Insights</h3>
              <img src={benefits_1} alt="data"></img>
              <p>Unique Value Proposition: The marketplace will offer exclusive financial data and reports that are not readily available elsewhere. </p>
            </div>
            <div className="benefit-box">
              <h3>Incentivized Data Contribution</h3>
              <img src={benefits_2} alt="blockchain"></img>
              <p>Token Rewards for Contributors: Users who upload valuable financial data and reports are incentivized with token rewards.</p>
            </div>
          </div>
        </section>

        <img src={filler_img} className="filler-img"></img>

        <section className="core-services" ref={servicesRef}>
          <h2>Our Core Services</h2>
          <div className="services-container">
            <div className="service-card">
              <img src={card_img1} alt="Service 1" />
              <h3>Exclusive Market Insights</h3>
            </div>
            <div className="service-card">
              <img src={card_img2} alt="Service 2" />
              <h3>Decentralized Data Exchange</h3>
            </div>
            <div className="service-card">
              <img src={card_img3} alt="Service 3" />
              <h3>User-Generated Reports</h3>
            </div>
            <div className="service-card">
              <img src={card_img4} alt="Service 4" />
              <h3>Secure Data Storage</h3>
            </div>
          </div>
        </section>

        <div className="team-section" ref={teamRef}>
          <div className="team-info">
            <h1>OUR TEAM</h1>
            <h3>Utkarsh Gupta</h3>
            <p className="role">Creator and Founder</p>
            <p className="uni">University of Waterloo & Wilfrid Laurier University Student</p>
          </div>
          <div className="team-links">
            <a href="https://www.linkedin.com/in/utkarshg20" target="_blank" rel="noopener noreferrer">
              <img src={linkedinLogo} alt="LinkedIn" />
            </a>
            <a href="https://github.com/utkarshhh20" target="_blank" rel="noopener noreferrer">
              <img src={githubLogo} alt="GitHub" />
            </a>
          </div>
        </div>

        <section className="newsletter" ref={newsRef}>
          <div classname="newsletter">
            <img src={contact_img} alt="Contact us image" className="newsletter-img"></img>
          </div>
          <div className="newsletter-content">
            <h2>Don't Miss Our News And Updates!</h2>
            <p>Connecting You to the World: Fresh News, Regular Updates!</p>
            <form className="newsletter-form">
              <input type="email" placeholder="Enter your email" />
            </form>
          </div>
        </section>
        <footer>
        <p>&copy; 2023 ChainSpark. All rights reserved.</p>
      </footer>
      </main>
    </div>
  );
};

export default LandingPage;
