import React from "react";
import c1 from "../../assets/c1.png";

const BlogPost = () => {
  return (
    <div className="flex flex-wrap max-w-[1300px] w-[95%] mx-auto justify-between">
      <div className="flex w-[50%]">
        <img src={c1} alt="c1" />
        <div>
          <p
            className="text-[20px] tablet:text-[28px] font-[600] leading-8"
          >
            Alchohol Addiction: Signs , Recovery & Complications{" "}
          </p>
          <p className="text-[18px] tablet:text-[20px] font-[500] ">Hi guys, my wife caught me drinking alcohol,drinking it. </p>
          <p className="text-[16px] text-blue">Read more ...</p>
        </div>
      </div>

      <div className="flex w-[50%]">
        <img src={c1} alt="c1" />
        <div>
          <p
            className="text-[20px] tablet:text-[28px] font-[600] leading-8"
          >
            Alchohol Addiction: Signs , Recovery & Complications{" "}
          </p>
          <p className="text-[18px] tablet:text-[20px] font-[500] ">Hi guys, my wife caught me drinking alcohol,drinking it. </p>
          <p className="text-[16px] text-blue">Read more ...</p>
        </div>
      </div>

      <div className="flex w-[50%]">
        <img src={c1} alt="c1" />
        <div>
          <p
            className="text-[20px] tablet:text-[28px] font-[600] leading-8"
          >
            Alchohol Addiction: Signs , Recovery & Complications{" "}
          </p>
          <p className="text-[18px] tablet:text-[20px] font-[500] ">Hi guys, my wife caught me drinking alcohol,drinking it. </p>
          <p className="text-[16px] text-blue">Read more ...</p>
        </div>
      </div>
    </div>
  );
};

export default BlogPost;
