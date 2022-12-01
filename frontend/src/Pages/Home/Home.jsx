import React from "react";
<<<<<<< HEAD
import Appstats from '../../Components/AppStats/Appstats'
import {AiOutlineHeart} from 'react-icons/ai'
import {BiLineChart} from 'react-icons/bi'
import {TiFlashOutline} from 'react-icons/ti'
import people from '../../assets/Rectangle27.png';
import smiley from '../../assets/smileys.png';
import phones from '../../assets/Frame75.png';
import phone from '../../assets/Frame76.png';
import add from '../../assets/add.png';
=======
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
import Download from '../../Components/Download/Download'
import add from "../../assets/add.png";
>>>>>>> 38abc4457a0a7ad9e2c0cc374d9188254cb89ea2
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
<<<<<<< HEAD
        <img src={people} alt="people" />
      </section>

      <section><Appstats/></section>
=======
          <img src={peoples} alt="people" className="big_device" />
        <img src={people} alt="people" className="small_device" />
      </section>

      <section >
        <Appstats />
      </section>
>>>>>>> 38abc4457a0a7ad9e2c0cc374d9188254cb89ea2

      <section className="soberpal__home-third__section">
        <h1>You are not alone in the fight against addiction</h1>

        <div className="soberpal__home-third__section-cards ">
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
<<<<<<< HEAD
        <img src={phones} alt="phones" className='phones'/>
        <img src={phone} alt="phone" className='phone' />
        <div className="soberpal__home-fourth__section__flex">
          <div>
            <h4>Download the Soberpal app</h4>
            <p>Join over 200+ people already growing with Soberpal</p>
          </div>
          <button>Download App</button>
=======
        <img src={phones} alt="phones" className="big_device" />
        <img src={phone} alt="phone" className="small_device" />
        <div className="w-full tablet:w-[70%] max-w-[1000px] mx-auto">
          <Download />
>>>>>>> 38abc4457a0a7ad9e2c0cc374d9188254cb89ea2
        </div>
      <div className="w-full tablet:w-[85%] mx-auto mb-16 bg-blue h-[2px] my-6" />
      </section>


      <section className="soberpal__home-fifth__section">
        {/* <hr /> */}
        <div className="soberpal__home-fifth__section__padding">
          <h1>FAQs</h1>
          <p>
            Everything you need to go through the journey of reducing youur
            alcohol intake. These are frequently asked questions about the
            product. Dont find answer to your question?? send us a message.
          </p>
<<<<<<< HEAD
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
=======
          <div className="">
            <Faq
              question="Getting Started"
              answer="Signing up on Soberpal is easy and anonymous, we don't need any personal details from you. You only have to register with a username that will be unique to you within the app."
            />
            <div className="w-full tablet:w-[89%] mx-auto bg-black h-[2px] my-6" />

            <Faq
              question="What Is Soberpal?"
              answer="SoberPal is an app that helps you acheive your goal of becoming more conscious and decrease your liit on alcohol consumption. There is an easy and quick onboarding process which requires a nickname and avatar as all users will be anonymous."
            />
            <div className="w-full tablet:w-[89%] mx-auto bg-black h-[2px] my-6" />

            <Faq
              question="How Do I View My Total Progress"
              answer="You can view your progress by checking your dashboard. All you have to do is click on profile and click on My Dashboard to view your total progress."
            />
            <div className="w-full tablet:w-[89%] mx-auto bg-black h-[2px] my-6" />

            <Faq
              question="How Do I Change My Username?"
              answer="To change your username click Profile, click on Settings, beside your existing username, click edit. Type in your new username and click save."
            />
            <div className="w-full tablet:w-[89%] mx-auto bg-black h-[2px] my-6" />

            <Faq
              question="Reporting A Community Member."
              answer="To report a community member, click on Profile, click on Contact Us and send us an email in that regard."
            />
            <div className="w-full tablet:w-[89%] mx-auto bg-black h-[2px] my-6" />

            <Faq
              question="How Do I View My Private Message"
              answer="Your Private Messages can be view by going to your Profile and clicking on Private Messages, you'll be asked to input your unique security code, once it's confirmed your Private Meassages will be accessible. "
            />
>>>>>>> 38abc4457a0a7ad9e2c0cc374d9188254cb89ea2
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
