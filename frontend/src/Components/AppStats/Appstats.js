import './appstats.scss'
import hands from "../../assets/hands.jpg";
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
          <div className="stats__data-container">
            {AppStat.map((stat) => (
              <div className="stats__data" key={stat.id}>
                <p className="count">{stat.count}</p>
                <p>{stat.text}</p>
              </div>
            ))}
          </div>
        </div>
      </section>
  )
}

export default AppStats