import React, { useState, useEffect } from "react";
import { GrClose } from "react-icons/gr";
import { useNavigate } from "react-router-dom";

const AddPosts = ({ setShowModal }) => {
  const [message, setMessage] = useState("");
  const [username, setUserName] = useState("");
  const [avatar, setAvatar] = useState("");
  const [isPending, setIsPending] = useState(false);
  const [changeState, setChangeState] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem("token");
    const user = localStorage.getItem("username");
    const avatar = localStorage.getItem("avatar");

    if (token) {
      setChangeState(true);
    }

    if (user) {
      // window.location.reload();
      setUserName(JSON.parse(user));
    }
    if (avatar) {
      setAvatar(JSON.parse(avatar));
    }
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    const post = { message };
    setIsPending(true);
    console.log(post);
    fetch("https://soberpal.hng.tech/api/forum", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(post),
    }).then((data) => {
        console.log(data)
      console.log("added");
      setIsPending(false);
    //   navigate("/communitypost");
    });
  };
  return (
    <div>
      <div className="justify-center items-center flex overflow-x-hidden overflow-y-auto fixed inset-0 z-50 outline-none focus:outline-none">
        <div className="relative w-[92%] tablet:w-[90%] laptop:w-[600px] mx-auto max-w-3xl">
          <div className="rounded-lg pt-8 px-6 pb-16 shadow-lg relative flex flex-col w-full bg-white outline-none focus:outline-none">
            <button
              className="text-[20px] "
              onClick={() => setShowModal(false)}
            >
              <GrClose />
            </button>

            <form onSubmit={handleSubmit}>
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

              <div className="flex gap-3 mt-6 h-[40px] ">
              <img className='w-[40px] h-[40px]' src={avatar} alt="" />
                <textarea
                  className="border-2 w-full rounded-lg border-[black] outline-2 outline-blue"
                  required
                  value={message}
                  onChange={(e) => setMessage(e.target.value)}
                ></textarea>
                {/* <p>{body}</p> */}
              </div>
              {!isPending && <button>Share</button>}
              {isPending && <button disabled>Share...</button>}
            </form>
          </div>
        </div>
      </div>
      <div className="opacity-50 fixed inset-0 z-40 bg-black"></div>
    </div>
  );
};

export default AddPosts;
