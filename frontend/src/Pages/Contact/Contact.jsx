import React from "react";
import { useState, useRef } from "react";
import "./contact.scss";
import { GrLocation } from "react-icons/gr";
import { BsTelephone } from "react-icons/bs";
import { BsInstagram } from "react-icons/bs";
import { AiOutlineFacebook } from "react-icons/ai";
import { ImTwitter } from "react-icons/im";
import mapImg from "../../assets/Map.png";
import { ThreeDots } from "react-loading-icons";
import { useForm } from "react-hook-form";
import { toast, ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import emailjs from "@emailjs/browser";

const Contact = () => {
  const [formData, setFormData] = useState({});
  const notify = () =>
    toast.success("Form Submitted Successfully", {
      position: toast.POSITION.TOP_CENTER,
    });

  const form = useRef();

  const sendEmail = () => {
    emailjs
      .sendForm(
        "service_i5yysql",
        "template_usa8sis",
        form.current,
        "kWxi_dTDg52yCrF9v"
      )
      .then(
        (result) => {
          console.log(result.text);
        },
        (error) => {
          console.log(error.text);
        }
      );
  };

  const {
    register,
    getValues,
    handleSubmit,
    reset,
    formState: { errors },
  } = useForm({
    mode: "onSubmit",
    defaultValues: {
      name: "",
      email: "",
      message: "",
    },
  });

  const [spinner, setSpinner] = useState(false);

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
      })
      .catch((err) => {
        console.log(err.message);
      });
  };

  console.log(formData, "working");

  const onSubmit = () => {
    fetchData();
    sendEmail();
    reset();
    notify();
  };

  return (
    <div className="contact">
      <header>
        <ToastContainer autoClose={2000} />
        <h1>Contact Us</h1>
        <p>You can always reach out to us. We wil be glad to hear from you</p>
      </header>
      <div className="contact__content-section">
        <div className="section__one">
          <h2>Get in touch with us. How can we help?</h2>
          {/* form container */}

          <form ref={form} id="form" onSubmit={handleSubmit(onSubmit)}>
            {/* full-name input */}
            <div className="input__container">
              <label>Name</label>
              <input
                className={`${errors.name?.message ? "input__border" : ""}`}
                name="name"
                type="text"
                {...register("name", {
                  required: "Full name is required !!",
                  minLength: {
                    value: 6,
                    message: "Name should be at least 6 characters!!",
                  },
                })}
                placeholder="Omowunmi Olawehinmi"
              />
              {errors.name?.message ? (
                <p className="alert" role="alert">
                  {errors.name.message}
                </p>
              ) : (
                ""
              )}
            </div>

            {/* email input */}
            <div className="input__container">
              <label>Email</label>
              <input
                name="email"
                type="text"
                className={`${errors.email?.message ? "input__border" : ""}`}
                {...register("email", {
                  required: "Email is required!!",
                  pattern: {
                    value:
                      /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/,
                    message: "Email is invalid!!",
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
                className={`${errors.message?.message ? "input__border" : ""}`}
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
              // onClick={notify}
              type="submit"
              className={`${errors.message ? "btn__disabled" : ""}`}
              disabled={errors.message ? true : false}
            >
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
