import axios from "axios";
import { useState, useEffect } from "react";

// export const FormApi = (data) => {
//   axios.post("https://sober-pal.herokuapp.com/api/contact", {
//     body: data,
//     headers: {
//       "Content-Type": "application/json",
//     },
//   }).then(res => res.json());
// };

// export default FormData;

//   const [formData, setFormData] = useState([]);
//   console.log(formData, 'working')

//   fetch("https://sober-pal.herokuapp.com/api/contact", {
//     method: "POST",
//     body: JSON.stringify(data),
//     headers: {
//       "Content-type": "application/json; charset=UTF-8",
//     },
//   })
//     .then((res) => {
//       res.json();
//       setFormData(res)
//     })
//     .catch((err) => {
//       console.log(err.message);
//     });
