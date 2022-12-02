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
import { motion } from "framer-motion";

const NewsLetter = () => {
  const notify = () =>
    toast.success("Subscribed to Newsletter Successfully", {
      position: toast.POSITION.TOP_CENTER,
    });

  const form = useRef();

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors },
  } = useForm({
    mode: "onSubmit",
    defaultValues: {
      email: "",
      emailTop: ""
    },
  });

  const onSubmit = () => {
    reset();
    notify();
  };
  const onSubmitTop = () => {
    reset();
    notify();
  };

  return (
    <div className="newsletter">
      <header>
        {!errors.message && <ToastContainer autoClose={2000} />}
        <motion.h3
          whileInView={{ y: [100, 30], opacity: [0, 0, 1] }}
          transition={{ duration: 1.2 }}
        >
          NewsLetter
        </motion.h3>
        <motion.h1
          whileInView={{ y: [100, 30], opacity: [0, 0, 1] }}
          transition={{ duration: 1.2 }}
        >
          Subscribe to our newsletter
        </motion.h1>
        <motion.p
          whileInView={{ y: [100, 30], opacity: [0, 0, 1] }}
          transition={{ duration: 1.2 }}
        >
          We provide our network of customers, prospects and subbscriers
          <br />
          with relevant and valuable information about our latest products
          <br />
          and updates.
        </motion.p>
      </header>
      <section className="newsletter__one">
        <div className="newsletter__one-part">
          <motion.div
            whileInView={{ y: [100, 30], opacity: [0, 0, 1] }}
            transition={{ duration: 1.2 }}
          >
            <CheckDetails text="Weekly, bi-weekly, monthly email newsletters" />
            <CheckDetails text="Access to our social media community" />
            <CheckDetails text="Amazing tips on how to stay sober" />
          </motion.div>

          <form ref={form} onSubmit={handleSubmit(onSubmitTop)}>
            <motion.input
              whileInView={{ y: [100, 30], opacity: [0, 0, 1] }}
              transition={{ duration: 1.2 }}
              className={`${errors.emailTop?.message ? "input__border" : ""}`}
              {...register("emailTop", {
                required: "Email is required!!",
                pattern: {
                  value:
                    /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/,
                  message: "Email is invalid!!",
                },
              })}
              placeholder="Enter your email address"
            />
            {errors.emailTop?.message && (
              <p className="alert" role="alert">
                {errors.emailTop.message}
              </p>
            )}
            <motion.button
              whileInView={{ y: [100, 30], opacity: [0, 0, 1] }}
              transition={{ duration: 1.2 }}
              type=""
              className="btn__subscribe"
            >
              Subscribe
            </motion.button>
          </form>

          <motion.p
            whileInView={{ y: [100, 30], opacity: [0, 0, 1] }}
            transition={{ duration: 1.2 }}
          >
            <span>Join the 10,000</span> users that receive our weekly
            newsletter
          </motion.p>
        </div>
        <div className="newsletter__two-part">
          <motion.img
            whileInView={{ y: [100, 30], opacity: [0, 0, 1] }}
            transition={{ duration: 1.2 }}
            src={newsletterImg}
            alt="newsletterimg"
          />
        </div>
      </section>
      <motion.section
        whileInView={{ y: [100, 30], opacity: [0, 0, 1] }}
        transition={{ duration: 1.2 }}
        className="author__newsletter"
      >
        <motion.div
          whileInView={{ y: [100, 1], opacity: [0, 0, 1] }}
          transition={{ duration: 1.2 }}
          className="author__container"
        >
          <img src={Maradel} alt="" />
          <div>
            <p className="author__name">Maradel</p>
            <p>Author of newsletter</p>
          </div>
        </motion.div>
        <motion.div
          whileInView={{ y: [100, 1], opacity: [0, 0, 1] }}
          transition={{ duration: 1.2 }}
          className="author__content"
        >
          <h2>About our Newsletter</h2>
          <p>
            Our newsletter provides our users, subscribers, customers and
            prospects with different information about Soberpal. Subscriers have{" "}
            <br />
            the option of choosing to recieve newsletters from us weekly,
            bi-weekly or monthly.
          </p>
        </motion.div>
        <Link className="li">More about Maradel</Link>
      </motion.section>

      <motion.section
        whileInView={{ y: [100, 1], opacity: [0, 0, 1] }}
        transition={{ duration: 1.2 }}
        className="recent__news"
      >
        <h1>Recent News</h1>
        <p>
          We provide top notch and interesting newsletters. elow are some
          examples
        </p>
        <div className="newscard__container">
          <NewsCard />
        </div>
      </motion.section>

      <motion.section
        whileInView={{ y: [100, 1], opacity: [0, 0, 1] }}
        transition={{ duration: 1.2 }}
        className="newsletter__socials"
      >
        <h5>Follow us</h5>
        <motion.div
          whileInView={{ y: [100, 1], opacity: [0, 0, 1] }}
          transition={{ duration: 1.2 }}
          className="newsletter__icons"
        >
          <div className="icon__container-newsletter">
            <BsInstagram className="icon__newsletter" />
          </div>
          <motion.div
            whileInView={{ y: [100, 1], opacity: [0, 0, 1] }}
            transition={{ duration: 1.2 }}
            className="icon__container-newsletter"
          >
            <AiOutlineFacebook className="icon__newsletter" />
          </motion.div>
          <motion.div
            whileInView={{ y: [100, 1], opacity: [0, 0, 1] }}
            transition={{ duration: 1.2 }}
            className="icon__container-newsletter"
          >
            <ImTwitter className="icon__newsletter" />
          </motion.div>
        </motion.div>
      </motion.section>

      <motion.div
        whileInView={{ y: [100, 1], opacity: [0, 0, 1] }}
        transition={{ duration: 1.2 }}
        className="bottom__section"
      >
        <form ref={form} onSubmit={handleSubmit(onSubmit)}>
          <motion.input
            whileInView={{ y: [100, 1], opacity: [0, 0, 1] }}
            transition={{ duration: 1.2 }}
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
          <motion.button
            whileInView={{ y: [100, 1], opacity: [0, 0, 1] }}
            transition={{ duration: 1.2 }}
            type=""
            className="btn__subscribe"
          >
            Subscribe
          </motion.button>
        </form>
      </motion.div>

      <motion.div
        whileInView={{ y: [100, 1], opacity: [0, 0, 1] }}
        transition={{ duration: 1.2 }}
        className="download"
      >
        <div>
          <h6>Download the Soberpal app</h6>
          <p>Join over 200+ people already growing with Soberpal.</p>
        </div>
        <Button text="Download App" />
      </motion.div>
    </div>
  );
};

export default NewsLetter;
