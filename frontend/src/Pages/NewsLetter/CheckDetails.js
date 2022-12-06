import "./checkdetails.scss";
import { BsCheckCircleFill } from "react-icons/bs";

const CheckDetails = ({text}) => {
  return (
    <div className="checkdetails" >
      <BsCheckCircleFill className="icon" />
      <p>{text}</p>
    </div>
  );
};

export default CheckDetails;
