import { useEffect, useState } from 'react';


const useFetch = (url) => {
    const [data, setData] = useState(null);
    const [isLoading, setIsLoading] = useState(true);
    const [error, setError] = useState(null);

    
    
    const token = localStorage.getItem("token");
    const myHeaders = new Headers({
      'Authorization': `Bearer ${token} `,
    });
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
              console.log(res)
              if(!res.ok) {
                throw Error("Could not fetch data from that resource") 
              }
              return res.json();
            })
            .then(data => {
              console.log(data)
              setData(data);
              setIsLoading(false);
              setError(null);
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
        }, [token]);

    return { data, isLoading, error} 

}

export default useFetch;