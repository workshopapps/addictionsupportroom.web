import React from "react";
import { NavLink, Link } from "react-router-dom";
import BlogPost from "../../Components/BLog/BlogPost";
import Download from "../../Components/Download/Download";

const Forum = () => {
  return (
    <div>
      <div>
        <p className="font-[700] text-[30px] text-center mt-[30px] text-blue ">
          Blog
        </p>
        <p className="font-[700] text-[36px] laptop:text-[64px] text-center text-[#4F4F4F] mb-[10px] ">
          Addiction Insights
        </p>
        <p className="text-[16px] mx-auto w-[90%] tablet:w-[70%] laptop:w-[600px] tablet:text-[20px] text-center text-[#575757] mb-[20px] ">
          Thoughts and advices on addiction and challenges we face and advices
          from Industry experts
        </p>
      </div>

        {/* Blogs  */}

      <div>
        <BlogPost />
      </div>

      <section className="block laptop:flex laptop:flex-rol justify-between mx-auto w-[90%]"></section>
      <div className="w-full mb-[50px] mt-[90px] tablet:w-[70%] max-w-[1000px] mx-auto">
        <Download />
      </div>
      <br />
      <br />
    </div>
  );
};

export default Forum;
