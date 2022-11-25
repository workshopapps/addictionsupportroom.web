import "./about.scss";
import TeamData from "../../Data/TeamData";
import OurValues from "../../Components/ourvalues/OurValues";
import interview from "../../assets/interview.png";
import Job from "../../Components/jobcontainer/Job";
import Button from "../../UI/Button";
import ValueData from '../../Data/ValueData';
import AppStats from "../../Components/AppStats/Appstats";


const About = () => {
  return (
    <div  className="about__container">
      <header className="header" >
        <p className="about">About us</p>
        <h1>About Soberpal</h1>
        <p className="about__soberpal">
          Everything you need to go through the journey of reducing your alcohol
          intake. We’ve done the heavy lifting
          <br />
          so you don’t have to - the perfect starting point.
        </p>
        <p className="learn__more">Learn more about the team behind soberpal</p>
      </header>
       {/* app stats section */}
       <AppStats/>

      <div className="team">
        <h3>Meet our team</h3>
        <p>
          Our philosophy is simple — hire a team of diverse, passionate people
          and foster a culture <br />
          that empowers you to do you best work.
        </p>
        <div className="team__members">
          {/* Team Data */}
          {TeamData.map((data) => (
            <div className="member" key={data.id}>
              <img className="avatar" src={data.avatar} alt={data.name} />
              <p className="name">{data.name}</p>
              <p className="designation">{data.designation}</p>
            </div>
          ))}
        </div>
      </div>

      {/* ourvalues section */}
      <section className="center">
      <OurValues
      prg1='Our values'
      heading='How we work at soberpal'
      prg2='Our shared values keep us connected and guide us as one team'
      value={ValueData}
      />
      </section>

      {/* open postions section */}
      <section className="position">
        <p>Open positions</p>
        <h4>We’re looking for talented people</h4>
        <p className="position__text">
          We’re a 100% remote team spread all across the world. Join us!
        </p>
        <div className="interview">
          <img src={interview} alt="Interview" className="interview__img" />
        </div>
        {/* job container section */}
        <Job />
      </section>

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

export default About;
