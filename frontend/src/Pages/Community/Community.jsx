import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { toast, ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import CommunityPost from "../../Components/Community/CommunityPost";

const Community = () => {
  const [username, setUserName] = useState("");
  const [avatar, setAvatar] = useState("");

  const navigate = useNavigate();

  

  useEffect(() => {
    const token = sessionStorage.getItem("token");
    const user = sessionStorage.getItem("username");
    const avatar = sessionStorage.getItem("avatar");

    if (!token) {
      navigate("/community/login");
    }

    if (user) {
      setUserName(JSON.parse(user));
    }
    if (avatar) {
      setAvatar(JSON.parse(avatar));
    }
    // window.location.reload(false)
  }, []);

  return (
    <div className="">
      <ToastContainer />
      
      <div className=" community  h-[300px] tablet:h-[300px] desktop:h-[350px]">
        <div className="w-[95%] max-w-[1400px] h-full flex justify-center tablet:justify-end mx-auto e top-0">
          <div className="text-center mx-auto laptop:mx-0 my-auto w-fit font-[700] text-[48px] tablet:text-[68px] laptop:text-[74px] ">
            Welcome to <br />
            Our Community
          </div>
        </div>
      </div>

      <CommunityPost username={username} avatar={avatar} />
    </div>
  );
};

export default Community;
