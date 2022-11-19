import React from "react";
import Button from "../UI/Button";

const Download = () => {
  return (
    <div className="flex flex-col md:flex-row w-[261px] text-center md:text-start items-center md:w-full mx-auto md:justify-between py-3">
      <div>
        <h2 className="text-[32px] text-[#204E65] font-[500]">
          Download the Soberpal app
        </h2>
        <p className="text-[#575757] text-[20px] font-[400] mt-3">
          Join over 200+ people already growing with Soberpal.
        </p>
      </div>
      <button className="h-[44px] w-[131px] bg-[#204E65] rounded-[8px] text-white mt-4">
        Download app
      </button>
    </div>
  );
};

export default Download;
