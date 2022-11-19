import React from "react";
import Appstats from '../../Components/AppStats/Appstats'
import {AiOutlineHeart} from 'react-icons/ai'
import {BiLineChart} from 'react-icons/bi'
import {TiFlashOutline} from 'react-icons/ti'
import people from '../../assets/Rectangle27.png';
import smiley from '../../assets/smileys.png';
import phones from '../../assets/Frame75.png';
import phone from '../../assets/Frame76.png';
import add from '../../assets/add.png';
// import {people, smiley, phone, phones, add} from "./import";
import "./home.css";

const Home = () => {
const size = 40

  return (
    <div className="soberpal__home">
      <section className="soberpal__home-first__section">
        <h1>Guiding you from addiction to recovery</h1>
        <p>
          Soberpal is your reliable platform for addiction support. Our mission
          is to guide you to a healthier life and provide the support you
          need.
        </p>
        <img src={people} alt="people" />
      </section>

      <section><Appstats/></section>

      <section className="soberpal__home-third__section">
        <h1>You are not alone in the fight against addiction</h1>

        <div className="soberpal__home-third__section-cards">
          <div className="cards__padding">
            <div className="cards__flex">
              <AiOutlineHeart size={size} className='icon__round'/>
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
              <img src={smiley} alt="smileys" className='icon__round'/>
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
              <BiLineChart size={size}  className='icon__round'/>
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
              <TiFlashOutline size={50}  className='icon__padding'/>
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
          your progress, <br/>and live a more healtheir lifestyle with support from
          the community
        </p>
        <img src={phones} alt="phones" className='phones'/>
        <img src={phone} alt="phone" className='phone' />
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
            Everything you need to go through the journey of reducing youur
            alcohol intake. These are frequently asked questions about the
            product. Dont find answer to your question?? send us a message.
          </p>
          <div className="soberpal__home-fifth__section__flex1">
            <h3>What is Soberpal?</h3>
            <img src={add} alt="add" />
          </div>
          <hr />
          <div className="soberpal__home-fifth__section__flex1">
            <h3>Can I be anonymous?</h3>
            <img src={add} alt="add" />
          </div>
          <hr />
          <div className="soberpal__home-fifth__section__flex1">
            <h3>Do I get a personal sponsor?</h3>
            <img src={add} alt="add" />
          </div>
          <hr />
          <div className="soberpal__home-fifth__section__flex1">
            <h3>How does billing wor+k</h3>
            <img src={add} alt="add" />
          </div>
          <hr />
          <div className="soberpal__home-fifth__section__flex1">
            <h3>How do I change my account email</h3>
            <img src={add} alt="add" />
          </div>
        </div>
        <p className='display_none'>Don't find answer to your question?</p>
        <div className="soberpal__home-fifth__section__flexy">
          <div className="soberpal__home-fifth__section__flex2">
            <p>Ask us anything</p>
            <button>send</button>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Home;
