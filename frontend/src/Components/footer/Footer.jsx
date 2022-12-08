import React, { useState } from "react";
import { Link } from "react-router-dom";
import Newsletter from "../Newsletter/Newsletter";
import "./footer.css";
import logo from '../../assets/soberpal-logo.png'

const Footer = () => {


  const scrollUp = () => {
    window.scrollTo({ top: 0, left: 0, behavior: "smooth" });
  };





  return (
    <>
      <div className="soberpal__footer">
        <div className="soberpal__footer-flex">
          <div className="soberpal__footer-flex__box1">
            <img  src={logo} alt='Soberpal Logo' className="soberpal__logo"  />
            <h1>Soberpal</h1>
            <p>
              Creating an amazing experience for you on
              <br />
              your journey towards recovery
            </p>
          </div>
          <div className="soberpal__footer-flex__box2">
            <div>
              <p>Company</p>
              <Link onClick={scrollUp} to="/about">
                About us
              </Link>
              <Link onClick={scrollUp} to="/careers">
                Career
              </Link>
              <Link onClick={scrollUp} to="/contact">
                Contact us
              </Link>
              <Link onClick={scrollUp} to="/team">
                The Team
              </Link>
              <Link onClick={scrollUp} to="/faq">
                FAQs
              </Link>
            </div>
            <div>
              <p>Resources</p>
              <Link onClick={scrollUp} to="/blog">
                <a href="#blog">Blog</a>
              </Link>
              <Link onClick={scrollUp} to="/newsletter">
                Newsletter
              </Link>
              <Link onClick={scrollUp} to="/alcohol">
                {" "}
                Alcohol Addiction
              </Link>
            </div>
            <div>
              <p>Socials</p>
              <a href="https://twitter.com/SoberPal_NG/" >Twitter</a>
              <a href="https://www.instagram.com/soberpal_ng/" >Instagram</a>
              <a href="https://github.com/workshopapps/addictionsupportroom.web/" >Github</a>
            </div>
            <div>
              <p>Legal</p>
              <Link onClick={scrollUp} to="/terms_policy">Terms & Policy</Link>
            </div>
          </div>
        </div>
        <hr />
        <p>© 2022 Soberpal. All rights reserved. && </p>
      </div>

    </>
  );
};

export default Footer;
