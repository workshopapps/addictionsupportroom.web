import "./about.scss";
import TeamData from "../../Data/TeamData";
import OurValues from "../../Components/ourvalues/OurValues";
import interview from "../../assets/interview.png";
import Job from "../../Components/jobcontainer/Job";
import Button from "../../UI/Button";
import Download from '../../Components/Download/Download'

import ValueData from '../../Data/ValueData';
import AppStats from "../../Components/AppStats/Appstats";
import { motion } from 'framer-motion'


const About = () => {
  return (
    <div  className="about__container">
      <motion.header 
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.2, duration: 0.5 }}
        className="header" 
      >
        <p className="about">About us</p>
        <h1>About Soberpal</h1>
        <p className="about__soberpal">
          Everything you need to go through the journey of reducing your alcohol
          intake. We’ve done the heavy lifting
          <br />
          so you don’t have to - the perfect starting point.
        </p>
        <p className="learn__more">Learn more about the team behind soberpal</p>
      </motion.header>
       {/* app stats section */}
       <AppStats/>

      <motion.div 
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.2, duration: 0.5 }}
        className="team"
      >
        <h3>Meet our team</h3>
        <p>
          Our philosophy is simple — hire a team of diverse, passionate people
          and foster a culture <br />
          that empowers you to do you best work.
        </p>
        <div className="team__members">
          {/* Team Data */}
          {TeamData.map((data) => (
            <div className="member" key={data.id}>
              <img className="avatar" src={data.avatar} alt={data.name} />
              <p className="name">{data.name}</p>
              <p className="designation">{data.designation}</p>
            </div>
          ))}
        </div>
      </motion.div>

      {/* ourvalues section */}
      <motion.section 
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.2, duration: 0.5 }}
        className="center"
      >
      <OurValues
      prg1='Our values'
      heading='How we work at soberpal'
      prg2='Our shared values keep us connected and guide us as one team'
      value={ValueData}
      />
      </motion.section>

      {/* open postions section */}
      <motion.section 
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.2, duration: 0.5 }}
        className="position"
      >
        <p>Open positions</p>
        <h4>We’re looking for talented people</h4>
        <p className="position__text">
          We’re a 100% remote team spread all across the world. Join us!
        </p>
        <div className="interview">
          <img src={interview} alt="Interview" className="interview__img" />
        </div>
        {/* job container section */}
        <Job />
      </motion.section>

      <div className="w-full mb-16 tablet:w-[70%] max-w-[1000px] mx-auto">
          <Download />
        </div>
    </div>
  );
};

export default About;
