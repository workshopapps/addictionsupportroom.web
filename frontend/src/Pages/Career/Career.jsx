import React from "react";
import "./career.css";
import { Link } from "react-router-dom";
import arrow from "../../assets/Vector2.png";
import people from "../../assets/Frame2.png";
import OurValues from '../../Components/ourvalues/OurValues'
import ValueData from '../../Data/ValueData';
import ValueData2 from '../../Data/ValueData2';

const Career = () => {
  return (
    <div className="soberpal__career">
      <section className="soberpal__career-first__section">
        <div className="soberpal__career-first__section-box">
          <h1>
            <span>Grow</span> your Career with us at SoberPal
          </h1>
          <p>
            We are abunch of bold, creative and imaginative individuals
            collectively driving the effort of encouraging reduction in alcohol
            intake and ensuring people live a healthy lifestyle. Join us and
            contribute to this effort.
          </p>
          <button className="button__style">
          <Link to='job'>View all our open positions</Link>
          </button>
        </div>
        <img src={people} alt="people" />
      </section>

      <section className="soberpal__career-second__section">
        <h1>
          Join our mission to help 2 billion people <br /> break free from
          alcohol addiction
        </h1>
        <div className="soberpal__career-second__section-box">
          <div>
            <h3>200+</h3>
            <p>People reached</p>
          </div>
          <div>
            <h3>60%</h3>
            <p>Rate of recovery of our users</p>
          </div>
          <div>
            <h3>100+</h3>
            <p>5-star reviews</p>
          </div>
          <div>
            <h3>10k</h3>
            <p>Global downloads</p>
          </div>
        </div>
      </section>

      <section className="center">
      <OurValues
      prg1='Our values'
      heading='How we work at soberpal'
      prg2='Our shared values keep us connected and guide us as one team'
      value={ValueData}
      />
      </section>

      <section className="center">
      <OurValues
      prg1='Benefits'
      heading='Perks of working with us'
      prg2='We put people first and want to empower everybody at SoberPal to do their best work.'
      value={ValueData2}
      />
      </section>

      <section className="soberpal__career-third__section">
        <h4>open positions</h4>
        <h1>We're looking for talented people</h1>
        <p>We're 100% remote team spread all across the world. Join us!</p>
        <div className="soberpal__career-third__section-box">
          <Link to='job'>
            Senior moderator <img src={arrow} alt="arrow" />
          </Link>
          <Link to='job'>
            Product designer <img src={arrow} alt="arrow" />
          </Link>
          <Link to='job'>
            Front web developer <img src={arrow} alt="arrow" />
          </Link>
          <Link to='job'>
            Junior devops engineer <img src={arrow} alt="arrow" />
          </Link>
          <Link to='job'>
            Data analyst <img src={arrow} alt="arrow" />
          </Link>
          <Link to='job'>
            Ux writer <img src={arrow} alt="arrow" />
          </Link>
          <Link to='job'>
            Ux researcher <img src={arrow} alt="arrow" />
          </Link>
        </div>
      </section>
    </div>
  );
};

export default Career;
