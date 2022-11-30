import React from 'react'
import { Route, Routes } from 'react-router-dom';
import Home from '../Pages/Home/Home';

import Career from '../Pages/Career/Career';

import About from '../Pages/About/About';
import Contact from '../Pages/Contact/Contact';

import Faq from '../Pages/Faq/Faq'
import Team from '../Pages/Team/Team';

import TermsServices from '../Pages/TermsServices/TermsServices';
import Forum from '../Pages/Forum/Forum';
import Alcohol from '../Pages/Alcohol/Alcohol';
import JobApplication from '../Pages/JobApplication/JobApplication';


const CreateRoute = () => {
  return (
    <Routes>
      <Route path='/' element={<Home/>} />
      <Route path='careers' element={<Career/>} />
      <Route path='about' element={<About/>} />
      <Route path='contact' element={<Contact/>} />
      <Route path='faq' element={<Faq/>} />
      <Route path='team' element={<Team/>} />
      <Route path='forum' element={<Forum />} />
      <Route path='terms_policy' element={<TermsServices />} />
      <Route path='alcohol' element={<Alcohol />} />
      <Route path='careers/job' element={<JobApplication />} />

      {/* <Route path="*" element={<NotFound />} /> */}
    </Routes>
  )
}

export default CreateRoute;