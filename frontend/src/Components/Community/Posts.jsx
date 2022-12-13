import React, { useState } from "react";
import moment from "moment";
import { Link } from "react-router-dom";
import messageText from "../../assets/message-text.png";

const ComPosts = ({ posts }) => {
  const reversedPost = [...posts].reverse();

  const scrollUp = () => {
    window.scrollTo({ top: 0, left: 0, behavior: "smooth" });
  };

  return (
    <div className="w-[90%] mx-auto">
      {reversedPost.map((post) => (
        <Link key={post.id} to={`/communitypost/${post.id}`} onClick={scrollUp}>
          <div className="bg-white w-full my-5 p-5 rounded-lg">
            <div className="flex justify-between">
              <div className="flex gap-3 ">
                <img
                  className="w-[50px] h-[50px] border-2 border-[#BBBBBB] rounded-full"
                  src={post.user.avatar}
                  alt="avatar"
                />
                <div className="flex flex-col justify-between">
                  <p className="font-[500]">{post.user.username}</p>
                  <p className="text-[12px]">
                    {moment(post.date_posted)
                      .add(1, "hours")
                      .startOf("seconds")
                      .fromNow()}
                  </p>
                </div>
              </div>
            </div>
              <p className="mt-5">{post.message.slice(0, 150)} </p>
              <div className="flex gap-2 mt-3 items-center">
                <img
                  className="w-[20px] h-[20px]"
                  src={messageText}
                  alt="message"
                />
                <p className="hover:text-blue cursor-pointer text-[14px]">
                  {post.num_of_comments}
                </p>
              </div>
          </div>
        </Link>
      ))}
    </div>
  );
};

export default ComPosts;
