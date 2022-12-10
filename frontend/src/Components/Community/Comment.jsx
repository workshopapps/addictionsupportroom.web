import React, { useState, useEffect } from "react";
import useFetch from "../../API/userFetch";
// import { useParams } from "react-router-dom";

const Comment = ({post, idHandler}) => {
  const [message, setMessage] = useState("");
  const [username, setUserName] = useState("");
  const [avatar, setAvatar] = useState("");
  const [comment, setComment] = useState("");
  const [isPending, setIsPending] = useState(false);
  const [changeState, setChangeState] = useState(false);
  const [idhand, setIdHand] = useState(0);

//   const { postId } = useParams();
console.log(post)

  // const scrollUp = () => {
  //   window.scrollTo({ top: 0, left: 0, behavior: "smooth" });
  // };

  const token = localStorage.getItem("token");
  useEffect(() => {
    setIdHand(idHandler(post.id));
    const user = localStorage.getItem("username");
    const avatar = localStorage.getItem("avatar");

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
      owner: {
        username,
        avatar,
      },
      origin_post:{
        id: idHandler,
      },
      comment,
    };

    console.log(comments);
    setIsPending(true);
    fetch("https://soberpal.hng.tech/api/forum/comment/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify(comments),
    }).then((data) => {
        console.log(data)
      setIsPending(false);
      window.location.reload(false);
    });
    //   scrollUp();
  };

// const [message, setMessage] = useState("");
// const [username, setUserName] = useState("");
//   const [comment, setComment] = useState("");
// const [avatar, setAvatar] = useState("");
// const [isPending, setIsPending] = useState(false);
// const [changeState, setChangeState] = useState(false);

// // const navigate = useNavigate();

// const scrollUp = () => {
//   window.scrollTo({ top: 0, left: 0, behavior: "smooth" });
// };


// const token = localStorage.getItem("token");
// // console.log(token)
// useEffect(() => {
//     const user = localStorage.getItem("username");
//     const avatar = localStorage.getItem("avatar");

//   if (token) {
//     setChangeState(true);
//     console.log(changeState)
//   }

//   if (user) {
//     setUserName(JSON.parse(user));
//   }
//   if (avatar) {
//     setAvatar(JSON.parse(avatar));
//   }
// }, []);

// const handleSubmit = (e) => {
//   e.preventDefault();
//   const comments = { 
//       post_comments: [{
//         owner: {
//             username,
//             avatar,
//         },
//         comment,
//       }],
//   };
// //   setShowModal(false)

//   setIsPending(true);
//   console.log(comments);
//   fetch(`https://soberpal.hng.tech/api/forum/${post.id}`, {
//     method: "POST",
//     headers: { 
//       "Content-Type": "application/json",
//       'Authorization': `Bearer ${token}`,
//       },
//     body: JSON.stringify(comments),
//     }).then((data) => {
//       console.log(data)
//     setIsPending(false);
//     window.location.reload(false)
//   });
//   scrollUp();
// };
  return (
    <div>
      <form onSubmit={handleSubmit} className="flex border-2 border-[#BBBBBB] gap-3 mt-4 justify-between bg-white p-2 w-full rounded-[14px]">
        <div className="hidden">
          {/* <label>Post author</label> */}
          <input
            required
            className="border-2 border-[black] outline-2 outline-blue"
            onChange={(e) => setUserName(e.target.value)}
            value={username}
          />
          {/* <label>Post ima</label> */}
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
