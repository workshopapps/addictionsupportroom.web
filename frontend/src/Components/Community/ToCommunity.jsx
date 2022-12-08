import React from "react";
import { Link } from "react-router-dom";


const ToCommunity = () => {
  return (
    <div className="flex flex-col items-center pb-14">
      <div className="text-center px-5 md:px-0 md:w-[80%] font-[700]">
        <p className=" text-[32px] md:text-[57px]">
          Join 200,000+ Anonymous Soberpals,{" "}
          <span className="md:inline-block">
            Share Your Struggles And Accomplishmets
          </span>
        </p>
      </div>
      <div className=" px-7 md:w-[60%] text-center my-7">
        <p className="text-[14px] md:text-[18px] font-[400] text-[#575757]">
          We have a community of over 200+ soberpal members constantly sharing
          tips,{" "}
          <span className="md:inline-block">
            advices, experiences in our community section hencemaking each
            other’s journey easier .
          </span>
        </p>
      </div>
      <Link to="/community">
        <button className="h-[57px] w-[227px] bg-[#0E8ACB] rounded-[8px] text-white mt-4 hover--effect">
          Join The Community
        </button>
      </Link>
    </div>
  );
};

export default ToCommunity;
