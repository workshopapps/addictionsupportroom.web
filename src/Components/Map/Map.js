import { Wrapper, Status } from "@googlemaps/react-wrapper";
import { useState, useEffect, useRef } from "react";

import React from 'react'

 const Map = () => {
    
  const ref = useRef(null);
  const [map, setMap] = useState();

  useEffect(() => {
    if (ref.current && !map) {
      setMap(new window.google.maps.Map(ref.current, {}));
    }
  }, [ref, map]);
  return (
     <div ref={ref} />
  )
}

export default Map;
