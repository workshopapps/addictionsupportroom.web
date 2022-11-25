import { useState } from "react";
// import { Wrapper, Status } from "@googlemaps/react-wrapper";
import "./contact.scss";
import { GrLocation } from "react-icons/gr";
import { BsTelephone } from "react-icons/bs";
import { BsInstagram } from "react-icons/bs";
import { AiOutlineFacebook } from "react-icons/ai";
import { ImTwitter } from "react-icons/im";
import mapImg from "../../assets/Map.png";
// import Map from "../../Components/Map/Map";
// import { FormApi } from "../../API/FormApi";
import { ThreeDots } from "react-loading-icons";
import { useForm } from "react-hook-form";


const Contact = () => {
  const [formData, setFormData] = useState({});

  const {
    register,
    getValues,
    handleSubmit,
    reset,
    clearErrors,
    formState: { errors, isValid, isDirty },
    // reset,
  } = useForm({
    mode: "onSubmit",
    defaultValues: {
      name: "",
      email: "",
      message: "",
    },
  });

  const [spinner, setSpinner] = useState(false);
  const [disabled, setDisable] = useState(true);

  const fetchData = () => {
    fetch("https://sober-pal.herokuapp.com/api/contact", {
      method: "POST",
      body: JSON.stringify(getValues()),
      headers: {
        "Content-type": "application/json; charset=UTF-8",
      },
    })
      .then((res) => { 
        res.json();
        setFormData(res);
        setSpinner(false);
     
        // alert('Form Submitted Successfully')
      })
      .catch((err) => {
        console.log(err.message);
      });
  };


  console.log(formData, "working");
  

  const onSubmit = (data) => {
    console.log(data)
    fetchData();
    reset()
    clearErrors('email' && 'message' && 'name')
    alert("Form Submitted Successfully !!")
    console.log(getValues());
  };
  
   

  return (
    <div className="contact">
      <header>
        <h1>Contact Us</h1>
        <p>You can always reach out to us. We wil be glad to hear from you</p>
      </header>
      <div className="contact__content-section">
        <div className="section__one">
          <h2>Get in touch with us. How can we help?</h2>
          {/* form container */}

          <form id="form" onSubmit={handleSubmit(onSubmit)}>
            {/* full-name input */}
            <div className="input__container">
              <label>Name</label>
              <input
                className={`${
                  errors.name?.message ? "input__border" : ""
                }`}
                name="name"
                type="text"
                {...register("name", { required: "Full name is required !!", minLength: {
                  value: 6,
                  message: "Name should be at least 6 characters!!" 
                }})}
                placeholder="Omowunmi Olawehinmi"
              />
              {errors.name?.message && (
                <p className="alert" role="alert">
                  {errors.name.message}
                </p>
              )}
            </div>

            {/* email input */}
            <div className="input__container">
              <label>Email</label>
              <input
                name="email"
                type="text"
                className={`${
                  errors.email?.type === "required" || errors.email?.type === "pattern" ? "input__border" : ""
                }`}
                {...register("email", {
                  required: "Email is required!!",
                  pattern: {
                    value: /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/,
                    message: 'Email is invalid!!'
                  },
                })}
                placeholder="omowunmi2022@gmail.com"
              />
              {errors.email?.message && (
                <p className="alert" role="alert">
                  {errors.email.message}
                </p>
              )}
            </div>

            {/* message input */}
            <div className="input__container">
              <label>Message</label>
              <textarea
                cols=""
                rows="10"
                name="message"
                type="text"
                className={`${
                  errors.message?.type === "required" ? "input__border" : ""
                }`}
                {...register("message", { required: "Message is required!!" })}
                placeholder="Enter your message here..."
              />
              {errors.message?.message && (
                <p className="alert" role="alert">
                  {errors.message.message}
                </p>
              )}
            </div>
            <button
              type="submit"
              onClick={() => {
                onSubmit();
              }}>
              {spinner ? <ThreeDots /> : "Submit"}
            </button>
          </form>
        </div>
        {/* section two of the container */}
        <div className="section__two">
          {/* address section */}
          <div className="address__section">
            <div className="address">
              <GrLocation />
              <p>256, Newyork City, United States</p>
            </div>
            <div className="contact__details">
              <BsTelephone />
              <p>01 3456789</p>
            </div>
          </div>
          {/* social icons */}
          <div className="socials">
            <h3>Follow Us</h3>
            <div className="icons">
              <div className="icon__container">
                <BsInstagram className="icon" />
              </div>
              <div className="icon__container">
                <AiOutlineFacebook className="icon" />
              </div>
              <div className="icon__container">
                <ImTwitter className="icon" />
              </div>
            </div>
          </div>
          {/* map */}
          <div>
            <img src={mapImg} className="map" alt="Map" />
            {/* <Wrapper apiKey={"YOUR_API_KEY"}>
              <Map />
            </Wrapper> */}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Contact;
