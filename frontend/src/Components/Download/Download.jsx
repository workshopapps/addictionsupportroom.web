import React from "react";

const Download = () => {
  return (
    <div className="flex rounded-tl-[49px] rounded-br-[49px] rounded-tr-[20px] rounded-bl-[20px] bg-blue flex-col py-[100px] px-[100px] md:flex-row w-full text-center md:text-start items-center mobile:w-full mx-auto md:justify-between py-3">
      <div>
        <h2 className="text-[32px] text-white font-[500]">
          Download the Soberpal app
        </h2>
        <div className="text-white text-[20px] font-[400] mt-3">
          Join over 200+ people already growing with Soberpal.
        </div>
      </div>
      <button className="h-[44px] w-[131px] bg-white rounded-[8px] text-blue mt-4 hover--effect">
        Download app
      </button>
    </div>
  );
};

export default Download;
