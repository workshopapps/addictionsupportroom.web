import './appstats.scss'
import hands from "../../assets/hands.jpg";
import hand from "../../assets/Rectangle26.png";
import { motion } from 'framer-motion'
import AppStat from "../../Data/AppStat";

const AppStats = () => {
  return (
    <motion.section 
      whileInView={{y: [100, 0], opacity: [0,0,1]}} 
      transition={{ duration: 0.7 }}
      className="stats p-4 md:p-[3rem] mx-auto"
    >
      <div className=" mx-auto  flex justify-between gap-16 flex-wrap desktop:flex-nowrap max-w-[1300px]">
      <img src={hands} alt="hands mx-auto w-full " className="hands" />

      <div className="mt-[20px] mx-auto">
        <div 
          className="font-[700] text-left text-blue text-[16px] "
        >
          We’ve helped a couple of people reduce their intake of alcohol
        </div>
        <p className='text-left text-[34px] laptop:text-[40px] font-[600]'>
          We’re only just getting <br />
          started on our journey
        </p>
        
        <div className="flex flex-wrap justify-between w-[90%] laptop:w-[480px] mt-[20px]">

          <div className='w-[95%] mobile:w-[230px] '>
            <h3 className="text-[38px] laptop:text-[48px] text-start text-blue font-[600]">200+</h3>
            <p className="text-[18px] font-[500] text-start">People reached</p>
          </div>

          <div className='w-[95%] mobile:w-[230px]'>
            <h3 className="text-[38px] text-start laptop:text-[48px] text-blue font-[600]">60%</h3>
            <p className="text-[18px] text-start font-[500]">Rate of recovery of our users</p>
          </div>

          <div className='w-[95%] mobile:w-[230px]'>
            <h3 className="text-[38px] text-start laptop:text-[48px] text-blue font-[600]">10K</h3>
            <p className="text-[18px] text-start font-[500]">Global downloads</p>
          </div>

          <div className='w-[95%] mobile:w-[230px]'>
            <h3 className="text-[38px] text-start laptop:text-[48px] text-blue font-[600]">100+</h3>
            <p className="text-[18px] text-start font-[500]">5-star reviews</p>
          </div>
        </div>
      </div>
      </div>
    </motion.section>
  );
};

export default AppStats