import React, { useState, useEffect } from "react";

const Comment = ({post}) => {
  const [message, setMessage] = useState("");
  const [username, setUserName] = useState("");
  const [avatar, setAvatar] = useState("");
  const [comment, setComment] = useState("");
  const [isPending, setIsPending] = useState(false);
  const [changeState, setChangeState] = useState(false);

  const token = sessionStorage.getItem("token");
  useEffect(() => {
    const user = sessionStorage.getItem("username");
    const avatar = sessionStorage.getItem("avatar");

    // if (token) {
    //   setChangeState(true);
    // }

    if (user) {
      setUserName(JSON.parse(user));
    }
    if (avatar) {
      setAvatar(JSON.parse(avatar));
    }
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    const comments = {
      origin_post_id: post.id,
      comment,
    };

    setIsPending(true);
    fetch("https://soberpal.org/api/v2//forum/comment/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify(comments),
    }).then((data) => {
      setIsPending(false);
      window.location.reload(false);
    });
    //   scrollUp();
  };

  return (
    <div>
      <form
        onSubmit={handleSubmit}
        className="flex border-2 border-[#BBBBBB] gap-3 mt-4 justify-between bg-white p-2 w-full rounded-[14px]"
      >
        <div className="hidden">
          <input
            required
            className="border-2 border-[black] outline-2 outline-blue"
            onChange={(e) => setUserName(e.target.value)}
            value={username}
          />
          <input
            required
            className="border-2 border-[#BBBBBB] outline-2 outline-blue"
            value={avatar}
            onChange={(e) => setAvatar(e.target.value)}
          />
        </div>

        <img
          className="w-[40px] h-[40px] border-2 border-[#BBBBBB] rounded-full"
          src={avatar}
          alt="h"
        />
        <input
          type="text"
          className="w-full text-[14px] p-2 h-[40px] rounded-lg bg-[#F5F5F5]"
          placeholder="Post something to everyone"
          onChange={(e) => setComment(e.target.value)}
          value={comment}
        />
        <button className="py-2 px-4 bg-blue rounded-md text-white">
          Share
        </button>
      </form>
    </div>
  );
};

export default Comment;
