import { useEffect, useState } from 'react';


const useFetch = (url) => {
    const [data, setData] = useState(null);
    const [isLoading, setIsLoading] = useState(true);
    const [error, setError] = useState(null);
    const [scroll] = useState(true)

    
    
    const token = localStorage.getItem("token");
    const myHeaders = new Headers({
      'Authorization': `Bearer ${token} `,
    });

    const scrollUp = () => {
      window.scrollTo({ top: 0, left: 0, behavior: "smooth" });
    };

    useEffect(() => {
          const abortCont = new AbortController();
        //  setTimeout (() => {
          fetch(url, { 
            method: "GET",
            headers: myHeaders,
            signal: abortCont.signal
          }
            )
            .then(res => {
              // console.log(res)
              if(!res.ok) {
                throw Error("Could not fetch data from that resource") 
              }
              return res.json();
            })
            .then(data => {
              // console.log(data)
              setData(data);
              setIsLoading(false);
              setError(null);
              scrollUp(scroll)
            })
            .catch(err => {
              if (err.name === 'AbortError') {
                console.log("fetch abort")
              } else {
                setError(err.message);
                setIsLoading(false)
              }
            })
        //  }, 1000)
            return () => abortCont.abort();
        }, [url, token]);

    return { data, isLoading, error} 

}

export default useFetch;