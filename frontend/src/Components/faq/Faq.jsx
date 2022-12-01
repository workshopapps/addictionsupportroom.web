import React, { useState } from "react";
import add from '../../assets/add.png';
import './faq.css'
import { AiOutlinePlus } from "react-icons/ai";

const Faq = ({ question, answer }) => {
  const [click, setClick] = useState(false);

  return (
    <div className="w-[100%] mx-auto tablet:w-[89%] " >
      <div 
        onClick={() => setClick((prevstate) => !prevstate)}
        className="faq cursor-pointer"
      >
        <h3>{question}</h3>
        <img 
          src={add} alt='addImage'
        />
      </div>
      {click && 
        // <div className="bg-blue  mx-auto">
          <p className="ans">{answer}</p>
        // </div>
      }
    </div>
  );
};

export default Faq;
