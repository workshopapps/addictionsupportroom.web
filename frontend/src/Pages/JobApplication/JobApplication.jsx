import React from "react";
import { SlClock } from "react-icons/sl";
import { CiDollar } from "react-icons/ci";

const JobApp = () => {
  return (
    <div className="pt-20 w-[400px] md:w-[1007px] md:h-[902px] mx-auto p-6">
      <div className="flex justify-between">
        <div>
          <p className="text-[20px] md:text-[32px] font-[500] text-[#3E3E3E]">
            Senior Moderator
          </p>
          <div className="flex gap-5 mt-2">
            <div className="flex gap-2 items-center">
              <SlClock size={20} />
              <p className="text-[12px] md:text-[16px] font-[400] text-[#575757]">
                Full time
              </p>
            </div>
            <div className="flex gap-2 items-center">
              <CiDollar size={25} />
              <p className=" text-[12px] md:text-[16px] font-[400] text-[#575757]">
                20k - 30k
              </p>
            </div>
          </div>
        </div>
        <button className="px-[10px] w-[120px] h-[56px] md:w-[190px] bg-[#0E8ACB] rounded-[8px] text-white hover--effect">
          Apply now
        </button>
      </div>
      <div>
        <p className="mt-5 text-[14px] md:text-[20px] text-[#575757] font-[400]">
          We're seeking a Senior Controller to join our team. In this role, you
          will report to our Head of Finance and Operations, working to optimize
          our financial reporting to support effective decision-making.
        </p>
        <h1 className="mt-5 text-[16px] md:text-[22px] font-[500] text-[#575757]">
          What you will do
        </h1>
        <ul className="text-[14px] md:text-[20px] text-[#575757] font-[400] list-disc list-inside">
          <li>
            You will ensure that all rules of engagement amongst users in the
            chat room are observed
          </li>
          <li>
            You will ensure that user’s complaints are promptly attended to and
            resolved.
          </li>
        </ul>
        <h1 className="mt-5 text-[16px] md:text-[22px] font-[500] text-[#575757]">
          What we need
        </h1>
        <ul className="text-[14px] md:text-[20px] text-[#575757] font-[400] list-disc list-inside">
          <li>
            We need someone who shares our values and is ready to put in their
            best.
          </li>
          <li>
            You will ensure that user’s complaints are promptly attended to and
            resolved.
          </li>
        </ul>
        <h1 className="mt-5 text-[16px] md:text-[22px] font-[500] text-[#575757]">
          Benefits
        </h1>
        <ul className="text-[14px] md:text-[20px] text-[#575757] font-[400] list-disc list-inside">
          <li>Fully remote, flexible work day</li>
          <li>Monthly mental and physical health stipend</li>
          <li>Health insurance (country dependent)</li>
          <li>
            Flexible paid time off including holidays that are most meaningful
            to you
          </li>
        </ul>
        <h1 className="mt-5 text-[16px] md:text-[22px] font-[500] text-[#575757]">
          Apply for this Job
        </h1>
        <p className="text-[14px] md:text-[20px] font-[400] text-[#575757]">
          Please send us your Resume or LinkedIn profile at{" "}
          <a
            href="mailto:join@soberpal.com"
            className="underline text-[#204E65] hover:text-[#204e65ba]"
          >
            join@soberpal.com
          </a>
        </p>
      </div>
    </div>
  );
};

export default JobApp;
