import "./ourvalues.scss";

const OurValues = ({prg1, heading, prg2, value}) => {
  return (
    <div className="value">
      <header>
        <p>{prg1}</p>
        <h2>{heading}</h2>
        <p className="header__text">{prg2}</p> 
      </header>
      <section>
        {value.map((data) => (
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