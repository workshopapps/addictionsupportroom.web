import React, {useState} from "react";
import {  useNavigate } from 'react-router-dom';

import { GrClose } from "react-icons/gr";
import { toast, ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";


const ComModal = ({ setShowModal, setToken }) => {
    const [username, setUserName] = useState();
    const [avatar, setAvatar] = useState();

    const navigate = useNavigate();

    // const success = () =>
    // toast.success("Login Successfully", {
    //   position: toast.POSITION.TOP_CENTER,
    // });

    const faliure = () =>
    toast.error("Input correct password", {
      position: toast.POSITION.TOP_CENTER,
    });

    
    async function loginUser(credentials) {
        return fetch('https://soberpal.hng.tech/api/auth/login', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(credentials)
        })
          .then(data => data.json())
          .then(res => {console.log(res)
            localStorage.setItem("token", JSON.stringify(res.token));
            localStorage.setItem("username", JSON.stringify(username));
            localStorage.setItem("avatar", JSON.stringify(res.data.avatar));
            console.log(res.message)
            navigate("/community"); 
            }) 
            
          .catch(err => {console.log(err)
            faliure();
        })
    }
    
  
    const handleSubmit = async e => {
        e.preventDefault();
        const token = await loginUser({
          username,
    });
    setToken(token);
    }
  return (
    <>
      <div className="justify-center items-center flex overflow-x-hidden overflow-y-auto fixed inset-0 z-50 outline-none focus:outline-none">
        <ToastContainer />
        <div className="relative w-[92%] tablet:w-[90%] laptop:w-[600px] mx-auto max-w-3xl">
          <div className="rounded-lg py-16 shadow-lg relative flex flex-col w-full bg-white outline-none focus:outline-none">
            <button
              className="absolute text-[20px] top-8 right-8"
              onClick={() => setShowModal(false)}
            >
              <GrClose />
            </button>

            <div className="">
              <h3 className="text-[36px] text-center font-semibold">Log in</h3>
              <p className="text-[#575757] p-2 text-center my-5">
                Welcome back! Please enter your details{" "}
              </p>

              <form onSubmit={handleSubmit} className="mx-auto w-[92%] tablet:w-[80%] laptop:w-[400px]">
              {/* <form className="mx-auto w-[92%] tablet:w-[80%] laptop:w-[400px]"> */}
                <div className="flex flex-col mt-10">
                  <label className="text-[20px] font-[700]">Username</label>
                  <input
                    type="text"
                    name="username"
                    className="border-2 p-3 border-[black] rounded-lg mt-2 mb-5"
                    onChange={e => setUserName(e.target.value)}
                  />
                </div>

                <div className="flex">
                  <button
                    type="submit"
                    className="text-[18px] bg-blue text-white mt-5 py-2 px-6 mx-auto rounded-lg"
                  >
                    Sign In
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
      <div className="opacity-50 fixed inset-0 z-40 bg-black"></div>
    </>
  );
};

export default ComModal;
