import "./appstats.css";
import hands from "../../assets/hands.jpg";
import hand from "../../assets/Rectangle26.png";
import { motion } from 'framer-motion'
import AppStat from "../../Data/AppStat";

const AppStats = () => {
  return (
    <motion.section 
      whileInView={{y: [100, 50], opacity: [0,0,1]}} 
      transition={{ duration: 0.7 }}
      className="stats"
    >
      <div className="w-[93%] flex justify-between max-w-[1300px]">
      <img src={hands} alt="hands" className="hands" />
      <div className="stats__content">
        <div className="font-[700] text-blue ml-[-25px]">We’ve helped a couple of people reduce their inatke of alcohol</div>
        <h3>
          We’re only just getting <br />
          started on our journey
        </h3>
        {/* Stats data */}
        {/* {AppStat.map((stat) => (
          <div className="stats__data-container" key={stat.id}>
            <div>
              <h3 className="count"></h3>
              <p className="text">{stat.text}</p>
            </div>
          </div>
        ))} */}
        <div className="stats__data-container">
          <div>
            <h3 className="count">200+</h3>
            <p className="text">People reached</p>
          </div>

          <div>
            <h3 className="count">60%</h3>
            <p className="text">Rate of recovery of our users</p>
          </div>

          <div className="stats__mg-top">
            <h3 className="count">10K</h3>
            <p className="text">Global downloads</p>
          </div>

          <div className="stats__mg-top">
            <h3 className="count">100+</h3>
            <p className="text">5-star reviews</p>
          </div>
        </div>
        <img src={hands} alt="hands" className="hand" />
        <img src={hand} alt="hands" className="small__hand" />
      </div>
      </div>
    </motion.section>
  );
};

export default AppStats;
