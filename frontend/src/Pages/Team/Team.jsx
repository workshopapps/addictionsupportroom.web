import React from 'react'
import './Team.css'
import TeamData from "../../Data/TeamData";
import { AiFillLinkedin, AiFillTwitterSquare} from 'react-icons/ai';
import { motion } from 'framer-motion'
import Download from '../../Components/Download/Download';



const Team = () => {
   
  return (
    /* team--container-----containing everything in the team page */
    <div className="team__container">
      {/* team---text---contents */}
      <div className="team">
        <motion.div
          whileInView={{ y: [100, 30], opacity: [0, 0, 1] }}
          transition={{ duration: 1.2 }}
          className="team__text"
        >
          <span>The team</span>
          <h1>Meet the team behind Soberpal</h1>
          <p>
            We’re a small team that loves to create great experiences and make
            meaningful connections between builders and customers. Join our
            remote team!
          </p>
        </motion.div>

        {/* different team images */}
        <motion.div
          whileInView={{ y: [100, 30], opacity: [0, 0, 1] }}
          transition={{ duration: 1.2 }}
          className="team__img"
        >
          {/* mapped through my data file to access the images and informations */}
          {TeamData.map((data) => (
            <div className="team-info">
              <img src={data.avatar} alt="" />
              <h4>{data.name}</h4>
              <p>{data.designation}</p>
              <div className="flex w-[80px] mx-auto mt-5">
                <a
                  href={data.linkedIn}
                  className="text-[#0A66C2] hover:text-blue transition-all ease-in-out duration-300"
                >
                  <AiFillLinkedin
                    size={35}
                    style={{ borderRadius: "20px" }}
                  />
                </a>
                <a
                  href={data.twitter}
                  className="text-[#0165E1] hover:text-blue transition-all ease-in-out duration-1000"
                >
                  <AiFillTwitterSquare
                    size={35}
                    style={{ borderRadius: "20px" }}
                  />
                </a>
              </div>
            </div>
          ))}
        </motion.div>
      </div>

      {/* download app section */}
      <motion.div
        whileInView={{ y: [100, 10], opacity: [0, 0, 1] }}
        transition={{ duration: 1.3 }}
        className="team__download-app"
      >
        <div className="w-full mb-[50px] mt-[100px] tablet:w-[90%] max-w-[1400px] mx-auto">
          <Download />
        </div>
      </motion.div>
    </div>
  );
}

export default Team