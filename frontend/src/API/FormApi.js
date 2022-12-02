import axios from "axios";

export const FormApi = (data) => {
  const URL = `https://sober-pal.herokuapp.com/api/contact`
    axios
    .post(URL, {
      method: "post",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data),
     
    })
    .then((res) => {
      console.log(res)
    });
}

// https://sober-pal.herokuapp.com/api/contact