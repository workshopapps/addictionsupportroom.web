import "./contact.scss";
import { GrLocation } from "react-icons/gr";
import { BsTelephone } from "react-icons/bs";
import { BsInstagram } from "react-icons/bs";
import { AiOutlineFacebook } from "react-icons/ai";
import { ImTwitter } from "react-icons/im";
import Map from '../../assets/Map.png'

const Contact = () => {
  return (
    <div className="contact" >
      <header>
        <h1>Contact Us</h1>
        <p>You can always reach out to us. We wil be glad to hear from you</p>
      </header>
      <div className="contact__content-section">
        <div className="section__one">
          <h2>Get in touch with us. How can we help?</h2>
          {/* form container */}
          <form>
            <div className="input__container">
              <label>Name</label>
              <input
                type="text"
                name=""
                value=""
                placeholder="Omowunmi Olawehinmi"
              />
            </div>
            <div className="input__container">
              <label>Email</label>
              <input
                type="text"
                name=""
                value=""
                placeholder="omowunmi2022@gmail.com"
              />
            </div>
            <div className="input__container">
              <label>Message</label>
              <textarea
                cols=""
                rows="10"
                placeholder="Enter your message here..."
              />
            </div>
            <button type="submit">Submit</button>
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
           <img src={Map}  className="map"  alt="Map"/>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Contact;