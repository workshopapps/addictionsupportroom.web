import React from "react";
import { Link } from "react-router-dom";
import messageText from "../../assets/message-text.png";

const ComPosts = ({ posts }) => {
  return (
    <div className="w-[90%] mx-auto">
      {posts.map((post) => (
        <Link 
            key={post.id}
            to={`/communitypost/${post.id}`}
        >
          <div  className="bg-white w-full my-5 p-5 rounded-lg">
            <div className="flex gap-3">
              <img
                className="w-[50px] h-[50px]"
                src={post.user.avatar}
                alt="avatar"
              />
              <div className="flex flex-col justify-between">
                <p className="font-[500]">{post.user.username}</p>
                <p className="text-[12px]">{post.date_posted}</p>
              </div>
            </div>
            <p className="mt-5">{post.message}</p>
            <div className="flex gap-2 mt-3 items-center">
              <img
                className="w-[20px] h-[20px]"
                src={messageText}
                alt="message"
              />
              <p>comment</p>
            </div>
          </div>
        </Link>
      ))}
    </div>
  );
};

export default ComPosts;
