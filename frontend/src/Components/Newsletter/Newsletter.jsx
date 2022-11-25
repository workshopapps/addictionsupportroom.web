import React, { useState, useEffect } from "react";

const Newsletter = ({ closeHandler }) => {
  const [email, setEmail] = useState("");
  const [error, setError] = useState("");
  const [dataIsCorrect, setDataIsCorrect] = useState(false);

  const handleChange = (e) => {
    setEmail(e.target.value);
  };

  const validation = (props) => {
    let error = "";
    if (!email) {
      console.log(email);
      error = "Email is required!";
    } else if (!/\S+@\S+\.\S+/.test(email)) {
      error = "Email is Invalid!";
    }

    return error;
  };
  const handleClick = (e) => {
    e.preventDefault();
    setError(validation(email));
    setDataIsCorrect(true);
  };

  useEffect(() => {
    if (error.length === 0 && dataIsCorrect) {
      setError("");
      alert("Thanks for subscribing");
      setEmail("");
    }
  }, [error]);

  return (
    <div className="fixed inset-0 backdrop-blur-sm bg-black bg-opacity-25 flex justify-center items-center z-50">
      <div className="w-[450px] h-[326px]">
        <div className="bg-black text-white rounded-lg p-7">
          <div className="flex justify-between px-6 pb-4">
            <p className="text-[20px] font-medium">Join Our Mailing List</p>
            <button
              className="text-white text-lg hover:scale-125 font-extralight"
              onClick={closeHandler}
            >
              X
            </button>
          </div>
          <hr className="bg-grey-200" />
          <div className="my-6">
            <p>
              Subscribe to our weekly emails and get Helpful tips to help you in
              your journey.
            </p>
          </div>
          <form className="flex flex-col mt-6 gap-8">
            <div className="flex flex-col">
              <input
                type="email"
                required
                name="email"
                value={email}
                onChange={handleChange}
                placeholder="Enter your email"
                className="border-b border-b-white outline-none bg-black p-2 "
              />
              {error ? (
                <span className="text-red-400 text-sm mt-1 pl-4">{error}</span>
              ) : null}
            </div>
            <button
              onClick={handleClick}
              className="bg-[#0E8ACB] hover:bg-[#0e89cbca] rounded-lg p-3"
            >
              Join Now!
            </button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default Newsletter;
