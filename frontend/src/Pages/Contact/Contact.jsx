import { useState, useEffect, useRef } from "react";
import { Wrapper, Status } from "@googlemaps/react-wrapper";
import "./contact.scss";
import { GrLocation } from "react-icons/gr";
import { BsTelephone } from "react-icons/bs";
import { BsInstagram } from "react-icons/bs";
import { AiOutlineFacebook } from "react-icons/ai";
import { ImTwitter } from "react-icons/im";
import mapImg from "../../assets/Map.png";
import Map from "../../Components/Map/Map";
// import { FormApi } from "../../API/FormApi";
import { ThreeDots } from "react-loading-icons";
import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import * as Yup from "yup";

const validationSchema = Yup.object().shape({
  name: Yup.string()
    .required("fullName is required")
    .min(6, "fullName must be at least 6 characters"),
  email: Yup.string().required("Email is required").email("Email is invalid"),
  message: Yup.string().required("Password is required"),
});

const Contact = () => {
  const [formData, setFormData] = useState([]);

  

  const {
    register,
    getValues,
    handleSubmit,
    formState: { errors, isValid, isDirty },
    // reset,
  } = useForm({
    resolver: yupResolver(validationSchema),
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
        setFormData(res.body);
        setSpinner(false);
      })
      .catch((err) => {
        console.log(err.message);
      });
  };

  if (!isDirty && !isValid) {
    console.log(formData, "working");
  }
  
  const onSubmit = (e) => {
   
      fetchData();
    

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
                style={{ borderColor: "1px solid red !important" }}
                name="name"
                type="text"
                {...register("name", { required: true, minLength: 4 })}
                placeholder="Omowunmi Olawehinmi"
              />
              {errors.name?.type === "required" && (
                <p className="alert" role="alert">
                  Full name is required
                </p>
              )}
              {errors.name?.type === "min" && (
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
                  pattern:"/^w+([.-]?w+)*@w+([.-]?w+)*(.w{2,3})+$/",
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

              // disabled={!isValid  || !isDirty }
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
