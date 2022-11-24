// import { useState, useEffect } from "react";
import "./contact.scss";
import { GrLocation } from "react-icons/gr";
import { BsTelephone } from "react-icons/bs";
import { BsInstagram } from "react-icons/bs";
import { AiOutlineFacebook } from "react-icons/ai";
import { ImTwitter } from "react-icons/im";
import Map from "../../assets/Map.png";
import { FormApi } from "../../API/FormApi";
import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import * as Yup from "yup";

const validationSchema = Yup.object().shape({
  fullName: Yup.string()
    .required("fullName is required")
    .min(6, "fullName must be at least 6 characters"),
  email: Yup.string().required("Email is required").email("Email is invalid"),
  message: Yup.string()
    .required("Password is required")
    .min(6, "Password must be at least 6 characters"),
});

const Contact = () => {
  const {
    register,
    getValues,
    handleSubmit,
    formState: { errors },
    reset,
  } = useForm({
    resolver: yupResolver(validationSchema),
    mode: "onChange",
    defaultValues: {
      fullName: "",
      email: "",
      message: "",
    },
  });

  const onSubmit = (e) => {
    // e.preventDefault();
    if (errors.fullName && errors.email && errors.message === true) {
      return errors;
    } else {
     FormApi(getValues());
    }
    // reset();
    console.log(getValues());
  };

  async function handleLogin(e) {
    await handleSubmit(onSubmit)(e);
}
handleLogin()
 

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
                  errors.fullName === true
                    ? `style={{border:1px solid red}}`
                    : ""
                }`}
                name="fullName"
                type="text"
                {...register("fullName", { required: true, minLength: 4 })}
                placeholder="Omowunmi Olawehinmi"
              />
              {errors.fullName?.type === "required" && (
                <p className="alert" role="alert">
                  Full name is required
                </p>
              )}
              {errors.fullName?.type === "min" && (
                <p className="alert" role="alert">
                  Full name must be 6 characters at least
                </p>
              )}
            </div>

            {/* email input */}
            <div className="input__container">
              <label>Email</label>
              <input
                name="email"
                type="text"
                {...register("email", {
                  required: true,
                  pattern:
                    "([!#-'*+/-9=?A-Z^-~-]+(.[!#-'*+/-9=?A-Z^-~-]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([!#-'*+/-9=?A-Z^-~-]+(.[!#-'*+/-9=?A-Z^-~-]+)*|[[\t -Z^-~]*])",
                })}
                placeholder="omowunmi2022@gmail.com"
              />
              {errors.email?.type === "required" && (
                <p className="alert" role="alert">
                  Email is required
                </p>
              )}
              {errors.email?.type === "pattern" && (
                <p className="alert" role="alert">
                  Email is invalid
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
                {...register("message", { required: true })}
                placeholder="Enter your message here..."
              />
              {errors.message?.type === "required" && (
                <p className="alert" role="alert">
                  Message is required
                </p>
              )}
            </div>
            <button
              type="submit"
              onClick={() => {
                onSubmit();
              }}
            >
              {" "}
              Submit{" "}
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
            <img src={Map} className="map" alt="Map" />
          </div>
        </div>
      </div>
    </div>
  );
};

export default Contact;
