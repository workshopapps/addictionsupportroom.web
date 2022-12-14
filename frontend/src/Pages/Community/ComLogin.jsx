import React, { useState } from "react";
import loadingImage from '../../assets/loading.png'
import 'react-toastify/dist/ReactToastify.css';
import ComModal from "../../Components/Community/ComModal";


export default function Login() {
  const [showModal, setShowModal] = useState(false);
  const [token, setToken] = useState();


  return (
    <div className="App">
      <div>
        <p className="font-[700] mt-20 text-[36px] laptop:text-[64px] text-center text-[black] mb-[10px] ">
          Community
        </p>
        <p className="text-[16px] mb-16 mx-auto w-[90%] tablet:w-[70%] laptop:w-[600px] tablet:text-[18px] text-center text-[black]">
          Get access to a community of over 200,000+ members sharing their pains, experiences, tips, stories on addiction, family and recovery.
        </p>
      </div>
      <div className=" mt-16 mb-10 ">
        <img className="w-[90%] max-w-[800px] max-h-[400px] mx-auto" src={loadingImage} alt="loading" />
      </div>
      <div className="flex flex-col">
        <p className="text-[30px] tablet:text-[34px] text-center font-[700] leading-10">Only Soberpals members can view community</p>
        <p className="text-[20px] tablet:text-[24px] mt-3 text-center font-[500]">Please sign in to continue</p>
        <button 
          className="text-[16px] mx-auto bg-blue my-8 rounded-md text-white p-3 hover:opacity-75"
          type="button"
          onClick={() => setShowModal(true)}
        >
          Sign In Username
        </button>
        <p className="text-[16px] text-center mb-10">You need to have an account on the mobile App before you can join the community</p>
      </div>

      <div className="flex rounded-tl-[49px] mb-[90px] rounded-br-[49px] rounded-tr-[20px] rounded-bl-[20px] bg-blue flex-col pt-[60px] pb-[60px] px-[10px] tablet:px-[60px] md:flex-row w-[95%] text-center md:text-start items-center mobile:w-[97%] mx-auto md:justify-between py-3">
        <div>
          <h2 className="text-[32px] text-white font-[500]">
            Become a soberpal member
          </h2>
          <div className="text-white text-[20px] font-[400] mt-3">
          Join a community over 200,000 people already 
          <br />
          growing with Soberpal.
          </div>
        </div>
        <a href="https://appetize.io/app/232d7qqi3lzmn422ecnxnjgj4q" rel="noreferrer" target="_blank" >
          <button className="h-[44px] w-[131px] bg-white rounded-[8px] text-blue mt-4 hover--effect ">
            Download App
          </button>
        </a>
      </div>

      {showModal && <ComModal setShowModal={setShowModal} />}
      
    </div>
  );
}