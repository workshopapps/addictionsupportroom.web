import "./ourvalues.scss";
import { motion } from 'framer-motion'

const OurValues = ({prg1, heading, prg2, value}) => {
  return (
    <div  className="value">
      <motion.header  whileInView={{y: [100, 30], opacity: [0,0,1]}} transition={{ duration: 1.2 }}>
        <p>{prg1}</p>
        <h2>{heading}</h2>
        <p className="header__text">{prg2}</p> 
      </motion.header>
      <section >
        {value.map((data) => (
          <motion.div   whileInView={{y: [100, 30], opacity: [0,0,1]}} transition={{ duration: 1.2 }} className="value__content">
            <div className="value__icon">{data.icon}</div>
            <p className="value__h1">{data.header}</p>
            <p
              className="value__p"
              dangerouslySetInnerHTML={{ __html: data.content }}
            ></p>
          </motion.div>
        ))}
      </section>
    </div>
  );
};

export default OurValues;