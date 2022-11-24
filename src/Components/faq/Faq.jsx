import React, { useState } from "react";
import add from '../../assets/add.png';
import './faq.css'
import { AiOutlinePlus } from "react-icons/ai";

const Faq = ({ question, answer }) => {
  const [click, setClick] = useState(false);

  return (
    <div >
      <div className="faq">
        <h3>{question}</h3>
        <img 
          src={add}
          onClick={() => setClick((prevstate) => !prevstate)}
        />
      </div>
      {click && <p className="ans">{answer}</p>}
    </div>
  );
};

export default Faq;
