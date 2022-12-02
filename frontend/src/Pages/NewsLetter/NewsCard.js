import { Link } from "react-router-dom";
import "./newscard.scss";
import { motion } from "framer-motion";
import NewsLetterData from "./NewsLetterData";

const NewsCard = () => {
  return (
    <>
      {NewsLetterData.map((data) => (
        <motion.div
          whileInView={{ y: [100, 1], opacity: [0, 0, 1] }}
          transition={{ duration: 1.2 }}
          className="newscard"
        >
          <div>
            <p className="news__id">{data.id}</p>
            <p>{data.date}</p>
          </div>
          <h4>{data.title}</h4>
          <p>{data.content}</p>
          <Link className="li">More</Link>
        </motion.div>
      ))}
    </>
  );
};

export default NewsCard;
