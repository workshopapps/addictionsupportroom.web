import { useRef } from "react";
import { Link } from "react-router-dom";
import CheckDetails from "./CheckDetails";
import "./newsletter.scss";
import newsletterImg from "../../assets/newsletter.png";
import Maradel from "../../assets/Maradel.png";
import NewsCard from "./NewsCard";
import { BsInstagram } from "react-icons/bs";
import { AiOutlineFacebook } from "react-icons/ai";
import { ImTwitter } from "react-icons/im";
import Button from "../../UI/Button";
import { useForm } from "react-hook-form";
import { toast, ToastContainer } from "react-toastify";

const NewsLetter = () => {
  const notify = () =>
    toast.success("Subscribed to Newsletter Successfully", {
      position: toast.POSITION.TOP_CENTER,
    });

  const form = useRef();

  const {
    register,
    getValues,
    handleSubmit,
    reset,
    formState: { errors },
  } = useForm({
    mode: "onSubmit",
    defaultValues: {
      message: "",
    },
  });

  const onSubmit = () => {
    reset();
    notify();
  };
  // const onSubmitTop = () => {
  //   reset();
  //   notify();
  // };

  return (
    <div className="newsletter">
      <header>
        {!errors.message && <ToastContainer autoClose={2000} />}
        <h3>NewsLetter</h3>
        <h1>Subscribe to our newsletter</h1>
        <p>
          We provide our network of customers, prospects and subbscriers
          <br />
          with relevant and valuable information about our latest products
          <br />
          and updates.
        </p>
      </header>
      <section className="newsletter__one">
        <div className="newsletter__one-part">
          <div>
            <CheckDetails text="Weekly, bi-weekly, monthly email newsletters" />
            <CheckDetails text="Access to our social media community" />
            <CheckDetails text="Amazing tips on how to stay sober" />
          </div>

          <form  ref={form} onSubmit={handleSubmit(onSubmit)} >
            <input
              className={`${errors.email?.message ? "input__border" : ""}`}
              {...register("email", {
                required: "Email is required!!",
                pattern: {
                  value:
                    /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/,
                  message: "Email is invalid!!",
                },
              })}
              placeholder="Enter your email address"
            />
            {errors.email?.message && (
              <p className="alert" role="alert">
                {errors.email.message}
              </p>
            )}
            <button  type="" className="btn__subscribe">
              Subscribe
            </button>
          </form>

          <p>
            <span>Join the 10,000</span> users that receive our weekly
            newsletter
          </p>
        </div>
        <div className="newsletter__two-part">
          <img src={newsletterImg} alt="newsletterimg" />
        </div>
      </section>
      <section className="author__newsletter">
        <div className="author__container">
          <img src={Maradel} alt="" />
          <div>
            <p className="author__name">Maradel</p>
            <p>Author of newsletter</p>
          </div>
        </div>
        <div className="author__content">
          <h2>About our Newsletter</h2>
          <p>
            Our newsletter provides our users, subscribers, customers and
            prospects with different information about Soberpal. Subscriers have{" "}
            <br />
            the option of choosing to recieve newsletters from us weekly,
            bi-weekly or monthly.
          </p>
        </div>
        <Link className="li">More about Maradel</Link>
      </section>

      <section className="recent__news">
        <h1>Recent News</h1>
        <p>
          We provide top notch and interesting newsletters. elow are some
          examples
        </p>
        <div className="newscard__container">
          <NewsCard />
          <NewsCard />
          <NewsCard />
        </div>
      </section>

      <section className="newsletter__socials">
        <h5>Follow us</h5>
        <div className="newsletter__icons">
          <div className="icon__container-newsletter">
            <BsInstagram className="icon__newsletter" />
          </div>
          <div className="icon__container-newsletter">
            <AiOutlineFacebook className="icon__newsletter" />
          </div>
          <div className="icon__container-newsletter">
            <ImTwitter className="icon__newsletter" />
          </div>
        </div>
      </section>

      <div className="bottom__section">
        <form ref={form}  onSubmit={handleSubmit(onSubmit)}>
          <input
            className={`${errors.email?.message ? "input__border" : ""}`}
            {...register("email", {
              required: "Email is required!!",
              pattern: {
                value:
                  /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/,
                message: "Email is invalid!!",
              },
            })}
            placeholder="Enter your email address"
          />
          {errors.email?.message && (
            <p className="alert" role="alert">
              {errors.email.message}
            </p>
          )}
          <button type="" className="btn__subscribe">
            Subscribe
          </button>
        </form>
      </div>

      <div className="download">
        <div>
          <h6>Download the Soberpal app</h6>
          <p>Join over 200+ people already growing with Soberpal.</p>
        </div>
        <Button text="Download App" />
      </div>
    </div>
  );
};

export default NewsLetter;
