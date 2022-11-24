import "./appstats.css";
import hands from "../../assets/hands.jpg";
import hand from "../../assets/Rectangle26.png";
import AppStat from "../../Data/AppStat";

const AppStats = () => {
  return (
    <section className="stats">
      <img src={hands} alt="hands" className="hands" />
      <div className="stats__content">
        <p>We’ve helped a couple of people reduce their inatke of alcohol</p>
        <h3>
          We’re only just getting <br />
          started on our journey
        </h3>
        {/* Stats data */}
        {/* {AppStat.map((stat) => (
          <div className="stats__data-container" key={stat.id}>
            <div>
              <h3 className="count"></h3>
              <p className="text">{stat.text}</p>
            </div>
          </div>
        ))} */}
        <div className="stats__data-container">
          <div>
            <h3 className="count">200+</h3>
            <p className="text">People reached</p>
          </div>

          <div>
            <h3 className="count">60%</h3>
            <p className="text">Rate of recovery of our users</p>
          </div>

          <div className="stats__mg-top">
            <h3 className="count">10K</h3>
            <p className="text">Global downloads</p>
          </div>

          <div className="stats__mg-top">
            <h3 className="count">100+</h3>
            <p className="text">5-star reviews</p>
          </div>
        </div>
        <img src={hands} alt="hands" className="hand" />
        <img src={hand} alt="hands" className="small__hand" />
      </div>
    </section>
  );
};

export default AppStats;
