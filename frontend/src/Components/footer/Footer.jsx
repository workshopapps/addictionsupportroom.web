import React, { useState } from "react";
import { Link } from "react-router-dom";
import Newsletter from "../Newsletter/Newsletter";
import "./footer.css";

const Footer = () => {
  const [openModal, setOpenModal] = useState(false);

  const openHandler = () => {
    setOpenModal(true);
  };

  const closeHandler = () => {
    setOpenModal(false);
  };

  return (
    <>
      <div className="soberpal__footer">
        <div className="soberpal__footer-flex">
          <div className="soberpal__footer-flex__box1">
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
              <Link to="/about">About us</Link>
              <Link to="/careers">Career</Link>
              <Link to="/contact">Contact us</Link>
              <Link to="/team">The Team</Link>
              <Link to="/faq">FAQs</Link>
            </div>
            <div>
              <p>Resources</p>
              <Link to="/forum">Forum</Link>
              <Link onClick={openHandler}>Newsletter</Link>
              <Link to="/alcohol"> Alcohol Addiction</Link>
            </div>
            <div>
              <p>Socials</p>
              <Link to="#">Twiiter</Link>
              <Link to="#">LinkedIn</Link>
              <Link to="#">Github</Link>
            </div>
            <div>
              <p>Legal</p>
              <Link to="/terms_policy">Terms & Policy</Link>
            </div>
          </div>
        </div>
        <hr />
        <p>© 2022 Soberpal. All rights reserved.</p>
      </div>
      {openModal && <Newsletter closeHandler={closeHandler} />}
    </>
  );
};

export default Footer;
