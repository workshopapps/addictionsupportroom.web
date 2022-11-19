import React from 'react'

const Alcohol = () => {
  return (
    <div className="min-w-[343px] md:max-w-[1100px] mx-auto px-4 md:px-8 py-10">
      <p className="text-[12px] md:text-[16px] font-[700] text-center text-[#387E9C]">
        Alcohol Addiction
      </p>
      <h1 className="text-[#48A1C8] md:text-[#204E65] text-[20px] md:text-[48px] font-[700] text-center">
        Alcohol Addiction and Abuse
      </h1>
      <p className="text-[13px] md:text-[18px] font-[400] text-center text-[#575757] mt-3 md:mt-0 p-3 md:p-0">
        Alcoholism is one of the most common addictions all over the world. The
        social acceptance of drinking can often lead to denial — and, if left
        untreated, severe consequences.
      </p>

      <div className="flex justify-center md:gap-10 text-[#1D475C] gap-5 text-[14px] md:text-[20px] font-[700] my-8">
        <a href="#symptoms" className="hover:opacity-80 duration-300">
          Symptoms
        </a>
        <a href="#complications" className="hover:opacity-80 duration-300">
          Complications
        </a>
        <a href="#treatment" className="hover:opacity-80 duration-300">
          Treatment
        </a>
        <a href="#outlook" className="hover:opacity-80 duration-300">
          Outlook
        </a>
      </div>
    </div>
  );
}

export default Alcohol