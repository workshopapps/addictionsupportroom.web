import "./about.scss";
import TeamData from "../../Data/TeamData";
import OurValues from "../../Components/ourvalues/OurValues";
import Download from "../../Components/Download/Download";
import ValueData from "../../Data/ValueData";
import AppStats from "../../Components/AppStats/Appstats";
import { motion } from "framer-motion";

const About = () => {
  return (
    <div className="about__container">
      <motion.header
        whileInView={{ y: [100, 0], opacity: [0, 0, 1] }}
        transition={{ duration: 0.7 }}
        className="header p-4"
      >
        <p className="about">About us</p>
        <h1>About Soberpal</h1>
        <p className="text-[black] text-[18px] tablet:text-[20px]">
          Everything you need to go through the journey of reducing your alcohol
          intake. We’ve done the heavy lifting
          <br />
          so you don’t have to - the perfect starting point.
        </p>
        <p className="learn__more ">Learn more about the team behind soberpal</p>
      </motion.header>
      {/* app stats section */}
      <motion.div
        whileInView={{ y: [100, 0], opacity: [0, 0, 1] }}
        transition={{ duration: 0.7 }}
        
      >
        <div className="bg-[#e9edf0]">
        <AppStats />
          
        </div>
      </motion.div>
      <motion.div
        whileInView={{ y: [100, 0], opacity: [0, 0, 1] }}
        transition={{ duration: 0.7 }}
        className="team__container"
      >
        <h1>The Team</h1>
        <h3>Meet The Team</h3>
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
        whileInView={{ y: [100, 0], opacity: [0, 0, 1] }}
        transition={{ duration: 0.7 }}
        className="center"
      >
        <OurValues
          prg1="Our values"
          heading="How we work at soberpal"
          prg2="Our shared values keep us connected and guide us as one team"
          value={ValueData}
        />
      </motion.section>


      <div className="w-full mb-[50px] mt-[80px] tablet:w-[90%] max-w-[1000px] mx-auto px-4">
        <Download />
      </div>
    </div>
  );
};

export default About;
