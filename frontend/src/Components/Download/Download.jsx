import React from "react";

const Download = () => {
  return (
    <div className="flex flex-col md:flex-row w-[95%] text-center md:text-start items-center mobile:w-full mx-auto md:justify-between py-3">
      <div>
        <h2 className="text-[32px] text-blue font-[500]">
          Download the Soberpal app
        </h2>
        <p className="text-[#575757] text-[20px] font-[400] mt-3">
          Join over 200+ people already growing with Soberpal.
        </p>
      </div>
      <button className="h-[44px] w-[131px] bg-blue rounded-[8px] text-white mt-4 hover--effect">
        Download app
      </button>
    </div>
  );
};

export default Download;
