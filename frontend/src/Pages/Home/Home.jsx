import React, { useState,useEffect } from "react";
import Faq from "../../Components/faq/Faq";
import { Link } from "react-router-dom";

// import Appstats from "../../Components/AppStats/Appstats";
import { AiOutlineHeart } from "react-icons/ai";
import { BiLineChart } from "react-icons/bi";
import { TiFlashOutline } from "react-icons/ti";
import HomeBg from "../../assets/bg-home.png";
import phone from "../../assets/phone.png";
// import cell2 from "../../assets/cell2.png";
import { BsChatDots } from "react-icons/bs";
import start from "../../assets/start.png";
// import phone from "../../assets/Frame76.png";
import Download from "../../Components/Download/Download";
import { motion } from "framer-motion";
// import add from "../../assets/add.png";
import "./home.css";
// import ToCommunity from "../../Components/Community/ToCommunity";
import Button from "../../UI/Button";
import ToCommunity from "../../Components/Community/ToCommunity";
import { toast, ToastContainer } from "react-toastify";

const Home = () => {
  const size = 40;
  const [email, setEmail] = useState("")

  const success = () =>
    toast.success("Email received! you will be contacted shortly", {
      position: toast.POSITION.TOP_CENTER,
    });

  const handleChange = (e) => {
    setEmail(e.target.value)
  }

  // Fecthing the lead list
  // useEffect(() => {
  //   const fetchData = async () =>{
  //     const result = await fetch("https://soberpal.hng.tech/api/home/faq");
  //     const jsonResult = await result.json()

  //     console.log(jsonResult)
  //   }
  //   fetchData()
  // },[])


  // Posting email to the db
  const handleSubmit = async (e) => {
    const myData = {
      "email" : email
    }
    e.preventDefault()
    const result = await fetch("https://soberpal.hng.tech/api/home/faq", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(myData),
    });
    const jsonResult = await result.json()
    console.log(jsonResult)
    success()
    setEmail("")
  }

  return (
    <div className="soberpal__home">
      <ToastContainer autoClose={2000} />
      <motion.section
        className="soberpal__home-first__section"
        whileInView={{ y: [100, 50], opacity: [0, 0, 1] }}
        transition={{ duration: 0.7 }}
      >
        <h1 className="text-[black]">
          Guiding you from alcohol addiction to recovery
        </h1>
        <p className="mb-10">
          Looking for a way to cut back on your alcohol intake and live a sober
          lifestyle? Soberpal is the perfect app for you! With one click you
          have access to a community willing to motivate and guide you. Track
          your progress and see results over time.
        </p>

        <a href="https://appetize.io/app/3tqubo6rf6nodzau3rez6v2r5u?device=pixel4&osVersion=11.0&scale=75">
          <Button text="Start your recovery journey" />
        </a>
        <img src={HomeBg} alt="people" className="big_device" />
        <img src={HomeBg} alt="people" className="small_device" />
      </motion.section>

      <motion.section
        whileInView={{ y: [100, 50], opacity: [0, 0, 1] }}
        transition={{ duration: 0.7 }}
      >
        <p className="mt-[70px] mb-[40px] text-[28px] font-[600] text-center">
          We’ve helped a couple of people reduce their intake of alcohol
        </p>
        <div className="flex flex-wrap justify-between mt-[20px] mb-[70px] ">
          <div className="w-[30opx] mx-auto">
            <p className="text-[48px] text-blue text-center font-[700]">60%</p>
            <p className="text-[20px] font-[500]  text-center">
              Rate of recovery of our users
            </p>
          </div>

          <div className="w-[300px] mx-auto">
            <p className="text-[48px] text-blue text-center font-[700]">200+</p>
            <p className="text-[20px] font-[500]  text-center">
              5-star reviews
            </p>
          </div>

          <div className="w-[300px] mx-auto">
            <p className="text-[48px] text-blue text-center font-[700]">10K</p>
            <p className="text-[20px] font-[500] text-center">
              Global downloads
            </p>
          </div>
        </div>
      </motion.section>

      <motion.section
        whileInView={{ y: [100, 50], opacity: [0, 0, 1] }}
        transition={{ duration: 0.7 }}
        className="soberpal__home-third__section"
      >
        <p className="text-[32px] text-center font-[700]">Our services</p>
        <p className="text-[18px] mt-[20px] mb-[50px] text-center font-[400]">
          You are not alone in the fight against addiction
        </p>

        <div className="soberpal__home-third__section-cards ">
          <div className="cards__padding">
            <div className="cards__flex">
              <AiOutlineHeart size={size} className="icon__round" />
              <h3>Progress Reports</h3>
            </div>
            <p>Keep track of your success journey and stay motivated.</p>
          </div>

          <div className="cards__padding">
            <div className="cards__flex">
              <BsChatDots size={size} className="icon__round" />
              <h3>Chat Room</h3>
            </div>
            <p>
              We help you identify the different types of alchol addiction, the
              health <br />
              implication and what needs to be done to reduce your alchol
              consumption.
            </p>
          </div>

          <div className="cards__padding">
            <div className="cards__flex">
              <BiLineChart size={size} className="icon__round" />
              <h3>Daily Notes</h3>
            </div>
            <p>
              You have a personal journal for everyday moods or urges which can
              serve as a reference in your sobriety journey.
            </p>
          </div>

          <div className="cards__padding">
            <div className="cards__flex">
              <TiFlashOutline size={50} className="icon__padding" />
              <h3>Support Team</h3>
            </div>
            <p>
              Get support from advocates and recovering addicts willing to help
              put you on the right path to recovery.
            </p>
          </div>
        </div>
      </motion.section>

      <motion.section
        whileInView={{ y: [100, 50], opacity: [0, 0, 1] }}
        transition={{ duration: 0.7 }}
        className="soberpal__home-fourth__section"
      >
        <main className="text-[32px] text-center font-[700]">
          How we can help You
        </main>
        <p className="text-[18px] mt-[20px] mb-[30px] text-center font-[400]">
          You are not alone in the fight against addiction
        </p>
        <div className="h-full w-[90%] max-w-[900px] flex flex-wrap ">
          <div className="mx-auto mt-[20px]">
            <img src={phone} alt="phones" className="h-[400px] w-auto " />
          </div>
          <div className="mt-[100px] tablet:mt-[50px] mx-auto">
            <div className="flex gap-4 h-auto items-center mx-auto">
              <p className="rounded-[100%] text-[white] bg-blue p-2 px-5 mr-[16px]">
                1
              </p>
              <p className="text-[16px]">Getting sober</p>
            </div>
            <div className="flex gap-4 h-auto items-center">
              <p className="rounded-[100%] text-[white] bg-blue p-2 px-5 mr-[16px]">
                2
              </p>
              <p className="text-[16px]">
                Daily motivation and progress tracker
              </p>
            </div>
            <div className="flex gap-4 h-auto items-center">
              <p className="rounded-[100%] text-[white] bg-blue p-2 px-5 mr-[16px]">
                3
              </p>
              <p className="text-[16px]">Community support</p>
            </div>
            <div className="flex gap-4 h-auto items-center">
              <p className="rounded-[100%] text-[white] bg-blue p-2 px-5 mr-[16px]">
                4
              </p>
              <p className="text-[16px]">Get help anytime</p>
            </div>
          </div>
        </div>
      </motion.section>

      <br />
      <br />
      <br />
      <br />
      <br />
      <br />
      <br />
      <br />
      <br />
      <br />
      <div className="bg-[#D8F2FF] h-full  mb-[100px] pb-[100px]">
        <motion.section
          whileInView={{ y: [100, 50], opacity: [0, 0, 1] }}
          transition={{ duration: 0.7 }}
          className="w-[90%] laptop:w-[70%] mx-auto"
        >
          <main className="text-[38px] text-center font-[700]">
            What people say about us
          </main>
          <p className="text-[18px] mt-[20px] mb-[60px] text-center font-[400]">
            You are not alone in the fight against addiction
          </p>

          <div className="flex max-w-[1000px] mx-auto flex-wrap justify-between ">
            <div className="bg-blue mt-[30px] mx-auto py-[40px] px-4 rounded-[16px] w-[300px]">
              <div className="flex gap-1">
                <img src={start} alt="start" />
                <img src={start} alt="start" />
                <img src={start} alt="start" />
                <img src={start} alt="start" />
                <img src={start} alt="start" />
              </div>
              <div>
                <p className="mt-[20px] text-[white]">Lion</p>
                <p className="mt-[20px] text-[white]">
                  Soberpal has been an amazing support, I've made a lot of
                  friends for life and there has been a major reduction in my
                  alcohol intake.
                </p>
              </div>
            </div>

            <div className="bg-[#F1A66F] mx-auto mt-[30px] py-[40px] px-4 rounded-[16px] w-[300px]">
              <div className="flex gap-1">
                <img src={start} alt="start" />
                <img src={start} alt="start" />
                <img src={start} alt="start" />
                <img src={start} alt="start" />
                <img src={start} alt="start" />
              </div>
              <div>
                <p className="mt-[20px] text-[white]">Dolphin</p>
                <p className="mt-[20px] text-[white]">
                  It's been fun hanging out on the SoberPal app, I get to keep
                  track of my progress and avoid relapses. It's a great app and
                  you should definitely try it out.
                </p>
              </div>
            </div>
          </div>
        </motion.section>
      </div>

      {/* <motion.section
        className="join__community"
        whileInView={{ y: [100, 50], opacity: [0, 0, 1] }}
        transition={{ duration: 0.7 }}
      >
        <h4>
          Join 200+ Anonymous Soberpals, <br />
          Share Your Struggles And Accomplishmets
        </h4>
        <p>
          We have a community of over 200+ soberpal members constantly sharing
          tips, <br />
          advices, experiences in our community section hencemaking each other’s
          journey easier .
        </p>

          <Link classname="mx-auto bg-blue w-fit" to="/communitypost">
            <p classname="mx-auto mt-4 py-3 w-fit px-4 bg-blue text-white">
             Join The Community
             </p>
          </Link>
         
      </motion.section> */}
      <ToCommunity />

      <motion.section
        whileInView={{ y: [100, 50], opacity: [0, 0, 1] }}
        transition={{ duration: 0.7 }}
        className="soberpal__home-fifth__section max-w-[1300px] mx-auto"
      >
        {/* <hr /> */}
        <motion.div
          whileInView={{ y: [100, 50], opacity: [0, 0, 1] }}
          transition={{ duration: 0.7 }}
          className="soberpal__home-fifth__section__padding"
        >
          <h1>FAQs</h1>
          <p>
            Everything you need to go through the journey of reducing your
            alcohol intake. These are frequently asked questions about the
            product. Can't find answer to your question? Send us a message.
          </p>

          <div className="">
            <Faq
              question="Getting Started"
              answer="Signing up on Soberpal is easy and anonymous, we don't need any personal details from you. You only have to register with a username that will be unique to you within the app."
            />
            <div className="w-full tablet:w-[89%] mx-auto bg-black h-[2px] my-6" />

            <Faq
              question="What Is Soberpal?"
              answer="SoberPal is an app that helps you acheive your goal of becoming more conscious and decrease your liit on alcohol consumption. There is an easy and quick onboarding process which requires a nickname and avatar as all users will be anonymous."
            />
            <div className="w-full tablet:w-[89%] mx-auto bg-black h-[2px] my-6" />

            <Faq
              question="How Do I View My Total Progress"
              answer="You can view your progress by checking your dashboard. All you have to do is click on profile and click on My Dashboard to view your total progress."
            />
            <div className="w-full tablet:w-[89%] mx-auto bg-black h-[2px] my-6" />

            <Faq
              question="How Do I Change My Username?"
              answer="To change your username click Profile, click on Settings, beside your existing username, click edit. Type in your new username and click save."
            />
            <div className="w-full tablet:w-[89%] mx-auto bg-black h-[2px] my-6" />

            <Faq
              question="Reporting A Community Member."
              answer="To report a community member, click on Profile, click on Contact Us and send us an email in that regard."
            />
            <div className="w-full tablet:w-[89%] mx-auto bg-black h-[2px] my-6" />

            <Faq
              question="How Do I View My Private Message"
              answer="Your Private Messages can be view by going to your Profile and clicking on Private Messages, you'll be asked to input your unique security code, once it's confirmed your Private Meassages will be accessible. "
            />
          </div>
        </motion.div>
        <motion.div
          whileInView={{ y: [100, 50], opacity: [0, 0, 1] }}
          transition={{ duration: 0.7 }}
        >
          <h3 className="text-center font-[500] text-[28px]">
            Have a question?
          </h3>
          <div className="soberpal__home-fifth__section__flexy">
            <form
              onSubmit={handleSubmit}
              className="soberpal__home-fifth__section__flex2"
            >
              <input
                className="placeholder:text-slate-400 pl-2 relative"
                type="email"
                name="email"
                value={email}
                onChange={handleChange}
                required
                id="email"
                placeholder="Enter your email"
              />
              <button>send</button>
            </form>
          </div>
          <div className="absolute left-20">
              {/* <span className="text-center">Enter a valid email</span> */}
          </div>
        </motion.div>
        <div className="w-full mb-[50px] mt-[150px] tablet:w-[100%] max-w-[1000px] mx-auto">
          <Download />
        </div>
      </motion.section>
    </div>
  );
};

export default Home;
