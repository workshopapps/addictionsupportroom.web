import React from "react";

const Download = () => {
  return (
    <div className="flex rounded-tl-[49px] mb-[90px] rounded-br-[49px] rounded-tr-[20px] rounded-bl-[20px] bg-blue flex-col py-[30px] px-[15px] mobile:py-[50px] mobile:px-[20px] tablet:px-[60px] md:flex-row w-full text-center md:text-start items-center mobile:w-full mx-auto md:justify-between download__padding">
      <div>
        <h2 className="text-[32px] text-white font-[500]">
          Download the Soberpal app
        </h2>
        <h3 className="text-white text-[20px] font-[400] mt-3">
          Join over 200+ people already growing with Soberpal.
        </h3>
      </div>
      <a
        href="https://appetize.io/app/eeysp57n33smvpijzflyzvhkee?device=pixel4&osVersion=11.0&scale=75"
        rel="noreferrer"
        target="_blank"
      >
        <button className="h-[44px] w-[131px] bg-white rounded-[8px] text-blue mt-4 hover--effect">
          Download App
        </button>
      </a>
    </div>
  );
};

export default Download;
