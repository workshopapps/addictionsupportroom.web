import './appstats.scss'
import hands from "../../assets/hands.jpg";
import hand from "../../assets/Rectangle26.png";
import { motion } from 'framer-motion'
import AppStat from "../../Data/AppStat";

const AppStats = () => {
  return (
    <motion.section 
      whileInView={{y: [100, 50], opacity: [0,0,1]}} 
      transition={{ duration: 0.7 }}
      className="stats "
    >
      <div className="w-[100%] mx-auto flex justify-between flex-wrap desktop:flex-nowrap max-w-[1300px]">
      <img src={hands} alt="hands mx-auto w-full " className="hands" />
      <div className="stats__content">
        {/* <main>
          
        </main> */}
        <div className="font-[700] text-blue text-center mx-auto text-[20px] tablet:text-[24px] ">We’ve helped a couple of people reduce their inatke of alcohol</div>
        <h3>
          We’re only just getting <br />
          started on our journey
        </h3>
        
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
      </div>
      </div>
    </motion.section>
  );
};

export default AppStats