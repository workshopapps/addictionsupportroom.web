import React from "react";
import Faq from "../../Components/faq/Faq";
import Appstats from "../../Components/AppStats/Appstats";
import { AiOutlineHeart } from "react-icons/ai";
import { BiLineChart } from "react-icons/bi";
import { TiFlashOutline } from "react-icons/ti";
import people from "../../assets/Rectangle25.png";
import peoples from "../../assets/Rectangle27.png";
import smiley from "../../assets/smileys.png";
import phones from "../../assets/Frame75.png";
import phone from "../../assets/Frame76.png";
import add from "../../assets/add.png";
// import {people, smiley, phone, phones, add} from "./import";
import "./home.css";

const Home = () => {
  const size = 40;

  return ( 
    <div className="soberpal__home">
      <section className="soberpal__home-first__section">
        <h1>The alcohol rehabilitation support you need.</h1>
        <p>
          We are with you on your journey to recovery from alcohol addiction.
        </p>
        <img src={peoples} alt="people" className="big_device" />
        <img src={people} alt="people" className="small_device" />
      </section>

      <section>
        <Appstats />
      </section>

      <section className="soberpal__home-third__section">
        <h1>You are not alone in the fight against addiction</h1>

        <div className="soberpal__home-third__section-cards">
          <div className="cards__padding">
            <div className="cards__flex">
              <AiOutlineHeart size={size} className="icon__round" />
              <h3>We support each other</h3>
            </div>
            <p>
              Our team of experts, advocates and recovering addicts are
              committed to helping you find the right recovery plan to rebuild
              your life
            </p>
          </div>

          <div className="cards__padding">
            <div className="cards__flex">
              <img src={smiley} alt="smileys" className="icon__round" />
              <h3>We care about you</h3>
            </div>
            <p>
              Help you to identify the different types of alcohol addiction, how
              the substances affect the body and what you can do for yourself to
              reduce or stop it once and for all
            </p>
          </div>

          <div className="cards__padding">
            <div className="cards__flex">
              <BiLineChart size={size} className="icon__round" />
              <h3>We care about your progress</h3>
            </div>
            <p>
              We have compiled a comprehensive list of resources to help you or
              a loved one find a support system or get immediate help for an
              addiction
            </p>
          </div>

          <div className="cards__padding">
            <div className="cards__flex">
              <TiFlashOutline size={45} className="icon__padding" />
              <h3>We provide the support you need</h3>
            </div>
            <p>
              find the support among our experts, advocates and recovering
              addicts that will work best for you and power your recovery
            </p>
          </div>
        </div>
      </section>

      <section className="soberpal__home-fourth__section">
        <h1>Cutting egde features to help track your progress</h1>
        <p>
          Powerful, self-serve product help you track your alcohol intake, track
          your progress, <br />
          and live a more healtheir lifestyle with support from the community
        </p>
        <img src={phones} alt="phones" className="big_device" />
        <img src={phone} alt="phone" className="small_device" />
        <div className="soberpal__home-fourth__section__flex">
          <div>
            <h4>Download the Soberpal app</h4>
            <p>Join over 200+ people already growing with Soberpal</p>
          </div>
          <button>Download App</button>
        </div>
      </section>

      <section className="soberpal__home-fifth__section">
        <hr />
        <div className="soberpal__home-fifth__section__padding">
          <h1>FAQs</h1>
          <p>
            At SoberPal, We know how daunting it can be to admit and be willing to seek help in matters such as alcohol addiction.
            <br/>
            <br/>
            We, also know that the more knowledge you have about the app its fuunctions, the easier it will be for you to stay committed to acheiving your sobriety goals.
            <br/>
            <br/>
            Here are some of the questions you might have and their responses.
          </p>
          <div className="soberpal__home-fifth__section__padding2">
            <Faq
              question="Getting Started"
              answer="Signing up on Soberpal is easy and anonymous, we don't need any personal details from you. You only have to register with a username that will be unique to you within the app."
            />
            <hr />

            <Faq
              question="What Is Soberpal?"
              answer="SoberPal is an app that helps you acheive your goal of becoming more conscious and decrease your liit on alcohol consumption. There is an easy and quick onboarding process which requires a nickname and avatar as all users will be anonymous."
            />
            <hr />

            <Faq
              question="How Do I View My Total Progress"
              answer="You can view your progress by checking your dashboard. All you have to do is click on profile and click on My Dashboard to view your total progress."
            />
            <hr />

            <Faq
              question="How Do I Change My Username?"
              answer="To change your username click Profile, click on Settings, beside your existing username, click edit. Type in your new username and click save."
            />
            <hr />

            <Faq
              question="Reporting A Community Member."
              answer="To report a community member, click on Profile, click on Contact Us and send us an email in that regard."
            />
            <hr />

            <Faq
              question="How Do I View My Private Message"
              answer="Your Private Messages can be view by going to your Profile and clicking on Private Messages, you'll be asked to input your unique security code, once it's confirmed your Private Meassages will be accessible. "
            />
          </div>
        </div>
        <p className="display_none">Don't find answer to your question?</p>
        <div className="soberpal__home-fifth__section__flexy">
          <div className="soberpal__home-fifth__section__flex2">
            <input placeholder="Ask us anything"/>
            <button>send</button>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Home;
