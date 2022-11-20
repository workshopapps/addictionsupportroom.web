import React from 'react'
import { Route, Routes } from 'react-router-dom';
import Home from '../Pages/Home/Home';
import Career from '../Pages/Career/Career';
// import About from '../Pages/About/About';
// import Contact from '../Pages/Contact/Contact';
// import Faq from '../Pages/Faq/Faq'
import Services from '../Pages/Services/Services';
import Forum from '../Pages/Forum/Forum';


const CreateRoute = () => {
  return (
    <Routes>
      <Route path='/' element={<Home/>} />
      <Route path='careers' element={<Career/>} />
      {/* <Route path='about' element={<About/>} /> */}
      {/* <Route path='contact' element={<Contact/>} /> */}
      {/* <Route path='faq' element={<Faq/>} /> */}
      <Route path='forum' element={<Forum />} />
      <Route path='services' element={<Services />} />
      {/* <Route path="*" element={<NotFound />} /> */}
    </Routes>
  )
}

export default CreateRoute;