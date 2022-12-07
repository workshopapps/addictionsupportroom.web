import React from 'react'
import './Team.css'
import TeamData from "../../Data/TeamData";
import Button from "../../UI/Button";
import TeamImg from '../../assets/team.png'
import TeamImgmobile from '../../assets/team-mobile.png'
import { AiFillLinkedin, AiFillTwitterSquare, AiOutlineClockCircle } from 'react-icons/ai';
import { AiOutlineDollar } from 'react-icons/ai';
import { motion } from 'framer-motion'
import Download from '../../Components/Download/Download';



const Team = () => {
    const download = 'Download app'
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

      {/* team positions being looked for */}
      <div className="Team__position">
        <motion.span
          whileInView={{ y: [100, 30], opacity: [0, 0, 1] }}
          transition={{ duration: 1.1 }}
        >
          Open positions
        </motion.span>
        <motion.h2
          whileInView={{ y: [100, 10], opacity: [0, 0, 1] }}
          transition={{ duration: 1.3 }}
        >
          We’re looking for talented people
        </motion.h2>
        <motion.p
          whileInView={{ y: [100, 10], opacity: [0, 0, 1] }}
          transition={{ duration: 1.3 }}
        >
          We’re a 100% remote team spread all across the world. Join us!
        </motion.p>
        <motion.img
          whileInView={{ y: [100, 30], opacity: [0, 0, 1] }}
          transition={{ duration: 1.3 }}
          src={TeamImg}
          alt=""
          id="teamImg"
        />
        <img src={TeamImgmobile} alt="" id="teamImgmobile" />

        {/* roles for team-positions */}
        <motion.div
          whileInView={{ y: [100, 10], opacity: [0, 0, 1] }}
          transition={{ duration: 1.3 }}
          className="team__position__roles"
        >
          {/* the design roles */}
          <div className="design">
            <h3 className="role__title">Design</h3>
            <div className="product__designer">
              <h3 className="role">Product Designer</h3>
              <p>
                We’re looking for a mid-level product designer to join our team.
              </p>
              <div className="role__desc__icons">
                <span>
                  <AiOutlineClockCircle /> Full time
                </span>
                <span>
                  <AiOutlineDollar /> 20k - 30k
                </span>
              </div>
            </div>
            <div className="product__designer">
              <h3 className="role">Product Designer</h3>
              <p>
                We’re looking for a mid-level product designer to join our team.
              </p>
              <div className="role__desc__icons">
                <span>
                  <AiOutlineClockCircle /> Full time
                </span>
                <span>
                  <AiOutlineDollar /> 40k - 60k
                </span>
              </div>
            </div>
          </div>

          {/* software development roles */}
          <div className="software__development">
            <h3 className="role__title">Software Development</h3>

            {/* frontend-development role under software development */}
            <div className="frontend__developer">
              <h3 className="role">Frontend developer</h3>
              <p>
                We’re looking for an experienced frontend developer to join our
                team.
              </p>
              <div className="role__desc__icons">
                <span>
                  <AiOutlineClockCircle /> Full time
                </span>
                <span>
                  <AiOutlineDollar /> 80k - 100k
                </span>
              </div>
            </div>
          </div>
        </motion.div>
      </div>

      {/* download app section */}
      <motion.div
        whileInView={{ y: [100, 10], opacity: [0, 0, 1] }}
        transition={{ duration: 1.3 }}
        className="team__download-app"
      >
        <div className="w-full mb-[50px] mt-[150px] tablet:w-[100%] max-w-[1000px] mx-auto">
          <Download />
        </div>
      </motion.div>
    </div>
  );
}

export default Team