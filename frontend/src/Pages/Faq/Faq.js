import React from "react";
import "./Faq.css";
import FaqData from "../../Data/FaqData";
import helpcenter from "../../assets/helpcenter.png";
import Button from "../../UI/Button";
import { motion } from "framer-motion";
import Faq from "../../Components/faq/Faq";

const Faqs = () => {
  return (
    /* faq__container----contains everything in the faq page */

    <div className="faq__container">
      {/* the help center----containing the text and image */}
      <motion.div
        whileInView={{ y: [100, 0], opacity: [0, 0, 1] }}
        transition={{ duration: 1 }}
        className="faq__help-center"
      >
        <div className="faq__help-center__text">
          <h1>Help centre</h1>
          <p className="faq__p">
            Support that is always online.Get all the help you need about the
            product here.
          </p>
        </div>
        <div className="faq__help-center__img">
          <img src={helpcenter} alt="" />
        </div>
      </motion.div>

      {/* the form in the faq page containing the input and button */}
      <motion.div
        whileInView={{ x: [100, 0], opacity: [0, 0, 1] }}
        transition={{ duration: 1, delay: 0.5 }}
        className="faq__form-question first__form"
      >
        <h4 className="faq__form__title">Have a question?</h4>

        {/* the form */}
        <form action="">
          <input
            type="email"
            name=""
            id=""
            placeholder="Enter your email adress"
          />
          {/* the send button in the form */}
          <Button text={FaqData.send} />
        </form>
      </motion.div>

      <hr className="faq__hr" />

      {/* the faq section */}
      <div className="faq__section2">
        <h2>FAQs</h2>
        <p className="faq__p">
          Everything you need to go through the journey of reducing your alcohol
          intake. These are frequently asked questions bout the product. Dont
          find answer to your question?? send us amessage..
        </p>

        {/* faq questions and answer */}
        <div className="faq__questions-answer-section">
          <Faq
            question="Getting Started"
            answer="Signing up on Soberpal is easy and anonymous, we don't need any personal details from you. You only have to register with a username that will be unique to you within the app."
          />
          <hr className="faq__border-bottom" />

          <Faq
            question="What Is Soberpal?"
            answer="SoberPal is an app that helps you acheive your goal of becoming more conscious and decrease your liit on alcohol consumption. There is an easy and quick onboarding process which requires a nickname and avatar as all users will be anonymous."
          />
          <hr className="faq__border-bottom" />

          <Faq
            question="How Do I View My Total Progress"
            answer="You can view your progress by checking your dashboard. All you have to do is click on profile and click on My Dashboard to view your total progress."
          />
          <hr className="faq__border-bottom" />

          <Faq
            question="How Do I Change My Username?"
            answer="To change your username click Profile, click on Settings, beside your existing username, click edit. Type in your new username and click save."
          />
          <hr className="faq__border-bottom" />

          <Faq
            question="Reporting A Community Member."
            answer="To report a community member, click on Profile, click on Contact Us and send us an email in that regard."
          />
          <hr className="faq__border-bottom" />

          <Faq
            question="How Do I View My Private Message"
            answer="Your Private Messages can be view by going to your Profile and clicking on Private Messages, you'll be asked to input your unique security code, once it's confirmed your Private Meassages will be accessible. "
          />
        </div>
      </div>

      {/* the form in the faq page containing the input and button */}
      <motion.div
        whileInView={{ x: [-100, 0], opacity: [0, 0, 1] }}
        transition={{ duration: 1 }}
        className="faq__form-question"
      >
        <h4 className="faq__form__title">Have a question?</h4>
        {/* the form */}
        <form action="">
          <input
            type="email"
            name=""
            id=""
            placeholder="Enter your email adress"
          />

          <Button text={FaqData.send} id="btn" />
        </form>
      </motion.div>

      {/* download soberpal app */}
      <motion.div
        whileInView={{ y: [100, 0], opacity: [0, 0, 1] }}
        transition={{ duration: 1 }}
        className="faq__download-app"
      >
        <div className="faq__download-app-text">
          <h3>Download the Soberpal app</h3>
          <p className="faq__p download__p">
            Join over 200+ people already growing with Soberpal.
          </p>
        </div>
        <div className="faq__download-app-btn">
          {/* download button */}
          <Button text={FaqData.download} id="btn" />
        </div>
      </motion.div>
    </div>
  );
};

export default Faqs;
