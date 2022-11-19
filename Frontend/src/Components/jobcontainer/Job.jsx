import "./job.scss";
import { BiTimeFive } from "react-icons/bi";
import { CiDollar } from "react-icons/ci";
import JobData from "../../Data/JobData";

const Job = () => {
  return (
    <>
      <div className="job">
        <h5>Design</h5>
        <div className="job__container">
          <h6>Product Designer</h6>
          <p>
            We’re looking for a junior-level product designer to join our team.
          </p>
          <div className="price__container">
            <div className="contract">
              <BiTimeFive />
              <p>Full time</p>
            </div>
            <div className="price">
              <CiDollar />
              <p>40k - 60k</p>
            </div>
          </div>
        </div>

        <div className="job__container">
          <h6>Product Designer</h6>
          <p>
          We’re looking for a mid-level product designer to join our team.
          </p>
          <div className="price__container">
            <div className="contract">
              <BiTimeFive />
              <p>Full time</p>
            </div>
            <div className="price">
              <CiDollar />
              <p>40k - 60k</p>
            </div>
          </div>
        </div>
      </div>

      <div className="job">
        <h5>Software Development</h5>
        <div className="job__container">
          <h6>Frontend developer</h6>
          <p>
          We’re looking for an experienced frontend developer to join our team.
          </p>
          <div className="price__container">
            <div className="contract">
              <BiTimeFive />
              <p>Full time</p>
            </div>
            <div className="price">
              <CiDollar />
              <p>80k - 100k</p>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default Job;