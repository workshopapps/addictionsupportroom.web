import React, { useState, useEffect } from "react";
import { GrClose } from "react-icons/gr";

const AddPosts = ({ setShowModal }) => {
  const [message, setMessage] = useState("");
  const [username, setUserName] = useState("");
  const [avatar, setAvatar] = useState("");
  const [isPending, setIsPending] = useState(false);
  const [changeState, setChangeState] = useState(false);

  
  const scrollUp = () => {
    window.scrollTo({ top: 0, left: 0, behavior: "smooth" });
  };


  const token = sessionStorage.getItem("token");
  useEffect(() => {
      const user = sessionStorage.getItem("username");
      const avatar = sessionStorage.getItem("avatar");

    if (token) {
      setChangeState(true);
      console.log(changeState)
    }

    if (user) {
      setUserName(JSON.parse(user));
    }
    if (avatar) {
      setAvatar(JSON.parse(avatar));
    }
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    const post = { 
        message,
        user: {
            username,
            avatar
        }
    };
    setShowModal(false)

    setIsPending(true);
    console.log(post);
    fetch("https://soberpal.hng.tech/api/v1/forum/", {
      method: "POST",
      headers: { 
        "Content-Type": "application/json",
        'Authorization': `Bearer ${token}`,
        },
      body: JSON.stringify(post),
      }).then((data) => {
        console.log(token)
      setIsPending(false);
      window.location.reload(false)
    });
    scrollUp();
  };
  return (
    <div>
      <div className="justify-center items-center flex overflow-x-hidden overflow-y-auto fixed inset-0 z-50 outline-none focus:outline-none">
        <div className="relative w-[92%] tablet:w-[90%] laptop:w-[600px] mx-auto max-w-3xl">
          <div className="rounded-lg pt-8 px-10 pb-16 shadow-lg relative flex flex-col w-full bg-white outline-none focus:outline-none">
            <button
              className="absolute right-[40px] text-[20px] "
              onClick={() => setShowModal(false)}
            >
              <GrClose />
            </button>

            <form onSubmit={handleSubmit} >
              <div className="hidden">
                <label>Post author</label>
                <input
                  required
                  className="border-2 border-[black] outline-2 outline-blue"
                  onChange={(e) => setUserName(e.target.value)}
                  value={username}
                />
                <label>Post ima</label>
                <input
                  required
                  className="border-2 border-[black] outline-2 outline-blue"
                  value={avatar}
                  onChange={(e) => setAvatar(e.target.value)}
                />
              </div>
                <p className="mt-8 font-[600] text-[20px]">Make a post</p>
              <div className=" gap-3 mt-6 ">
                <img className='w-[50px] h-[50px] border-2 border-[#BBBBBB] rounded-full mb-4' src={avatar} alt="" />
                <textarea
                  className="border-[1px] p-2 w-full h-[200px] rounded-lg border-[#BBBBBB] outline-2 outline-blue"
                  required
                  value={message}
                  onChange={(e) => setMessage(e.target.value)}
                />
              </div>
              {!isPending && 
                <button 
                    className="bg-blue py-2 px-3 text-white mt-4 rounded-lg"
                >
                    Share
                </button>
                }
              {isPending && 
              <button 
                    className="bg-blue p-4 text-white mt-4 rounded-lg"
                >
                    Share...
                </button>
              }
            </form>
          </div>
        </div>
      </div>
      <div className="opacity-50 fixed inset-0 z-40 bg-black"></div>
    </div>
  );
};

export default AddPosts;