import React,{ useState, useEffect } from 'react'
import {  useNavigate } from 'react-router-dom';
import { toast, ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import CommunityPost from '../../Components/Community/CommunityPost';

const Community = () => {
  const [username, setUserName] = useState("");
  const [avatar, setAvatar] = useState("");

  const success = () =>
    toast.success("Login Successfully", {
      position: toast.POSITION.TOP_RIGHT,
    });


  const navigate = useNavigate();
    
  const handleLogout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("user");
    window.location.href = "/#/community/login";
  };

  useEffect(() => {
    // success();
    const token = localStorage.getItem("token")
    const user = localStorage.getItem("username")
    const avatar = localStorage.getItem("avatar")

    if (!token) {
      navigate("/community/login")
    } else {
    }

    if (user) {
      setUserName(JSON.parse(user));
    }
    if (avatar) {
      setAvatar(JSON.parse(avatar));
    }
  }, [])

  return (
    <div className=''>
        <ToastContainer />
      {/* <div className='bg-white flex items-center px-3 w-[150px] absolute top-[1.7%] right-[5%]'>
        <img className='ml-5 w-[50px] h-[50px]' src={avatar} alt="" />
        <p className='ml-5 font-[500]'>{username}</p>
      </div> */}
      <br />
      <br />
      <button
        onClick={() => handleLogout()}
      >
        logout</button>
      <div className=' community  h-[300px] tablet:h-[350px] desktop:h-[450px]'>
        <div className='w-[95%] max-w-[1400px] h-full flex justify-center tablet:justify-end mx-auto e top-0'>
          <div className='text-center mx-auto laptop:mx-0 my-auto w-fit font-[700] text-[48px] tablet:text-[68px] laptop:text-[74px] '>
            Welcome to <br />Our Community
          </div>
        </div>
      </div>

      <CommunityPost username={username} avatar={avatar} />
    </div>
  )
}

export default Community