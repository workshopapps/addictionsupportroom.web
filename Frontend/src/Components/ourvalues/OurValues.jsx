import "./ourvalues.scss";
import { BiUser } from "react-icons/bi";
import ValueData from "../../Data/ValueData";

const OurValues = ({icon, header, content,}) => {
  return (
    <div className="value">
      <header>
        <p>Our Values</p>
        <h2>How we work at Soberpal</h2>
        <p className="header__text">
          Our shared values keep us connected and guide us as one team.
        </p>
      </header>
      <section>
        {ValueData.map((data) => (
          <div className="value__content">
            <div className="value__icon">{data.icon}</div>
            <p className="value__h1">{data.header}</p>
            <p
              className="value__p"
              dangerouslySetInnerHTML={{ __html: data.content }}
            ></p>
          </div>
        ))}
      </section>
    </div>
  );
};

export default OurValues;
