import React, { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import useFetch from "../../API/userFetch";

import { BsThreeDots } from "react-icons/bs";
import moment from "moment";

import messageText from "../../assets/message-text.png";
import Comment from "../../Components/Community/Comment";
import ComSection from "../../Components/Community/ComSection";

const PostDetails = () => {
  const [username, setUserName] = useState("");
  const [avatar, setAvatar] = useState("");
  const [deleteBtn, setDeleteBtn] = useState(false);

  const navigate = useNavigate();

  const { postId } = useParams();
  const {
    data: post,
    isPending,
    error,
  } = useFetch("https://soberpal.hng.tech/api/forum/" + postId);

  const token = sessionStorage.getItem("token");
  
  
  // useEffect(() => {
  //   const user = sessionStorage.getItem("username");
  //   const avatar = sessionStorage.getItem("avatar");

  // const token = localStorage.getItem("token");

  const handleDeletePost = () => {

    fetch("https://soberpal.hng.tech/api/forum/" + postId, {
      method: "DELETE",
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }).then((res) => {
      // console.log(res);
      navigate("/communitypost");
    });
  };


  useEffect(() => {
    const user = sessionStorage.getItem("username");
    const avatar = sessionStorage.getItem("avatar");
    if (token) {
      // setDeletePost(true)
    }
    if (user) {
      setUserName(JSON.parse(user));
    }
    if (avatar) {
      setAvatar(JSON.parse(avatar));
    }
  }, []);

  return (
    <div className="max-w-[800px] bg-[#F5F5F5] my-16 py-4 mx-auto w-full tablet:w-[90%] rounded-[14px]">
      {error && (
        <div className="text-blue text-[24px] font-[500] text-center">
          {error}
        </div>
      )}
      {isPending && (
        <div className="text-blue text-[24px] font-[500] text-center">
          Loading...
        </div>
      )}
      {post && (
        <section className="w-[90%] mx-auto mb-16">
          <div className=" mx-auto">
            <div className="bg-white w-full my-5 p-5 rounded-lg">
              <div className="flex justify-between items-center">
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
                {post.user.username === username ? (
                  <div className="relative">
                    <div onClick={() => setDeleteBtn(true)}>
                      <BsThreeDots className="cursor-pointer text-[20px] mr-2" />
                    </div>
                    {deleteBtn && (
                      <div className="absolute  top-0 left-[-18px] ">
                        <div className="mx-auto bg-white" onClick={() => setDeleteBtn(false)}>
                        <BsThreeDots className="mx-auto text-[20px] "/>
                      </div>
                      <div
                        onClick={handleDeletePost}
                        className="shadow-lg py-1 px-2 text-[12px] cursor-pointer rounded-md border-[1px] border-gray-400"
                      >
                        Delete
                      </div>
                      </div>
                    )}
                  </div>
                ) : null}
              </div>

              <p className="mt-5">{post.message}</p>
              <div className="flex gap-2 mt-3 items-center">
                <img
                  className="w-[20px] h-[20px]"
                  src={messageText}
                  alt="message"
                />
                <p>{post.num_of_comments}</p>
              </div>

              <hr className="bg-[#BBBBBB] h-[2px] mt-6 mb-4" />

              {/* Comment section  */}
              <Comment post={post} />
              <ComSection post={post} />
            </div>
          </div>
        </section>
      )}
    </div>
  );
};

export default PostDetails;
