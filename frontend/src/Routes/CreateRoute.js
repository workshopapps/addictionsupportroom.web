import React, {useState} from 'react'
import { Route, Routes } from 'react-router-dom';
import Home from '../Pages/Home/Home';

import Career from '../Pages/Career/Career';

import About from '../Pages/About/About';
import Contact from '../Pages/Contact/Contact';

import Faqs from '../Pages/Faq/Faq'
import Team from '../Pages/Team/Team';

import TermsServices from '../Pages/TermsServices/TermsServices';
import Blog from '../Pages/Blog/Blog';
import Alcohol from '../Pages/Alcohol/Alcohol';
import JobApplication from '../Pages/JobApplication/JobApplication';
import NewsLetter from '../Pages/NewsLetter/NewsLetter';
import Community from '../Pages/Community/Community';
import ComLogin from '../Pages/Community/ComLogin';
import PostDetails from '../Pages/Community/PostDetails';
import AddPosts from '../Pages/Community/AddPosts';
// import ProtectedRoute from './ProtectedRoute';


const CreateRoute = () => {

  const [token, setToken] = useState();
  // const token = sessionStorage.getItem('accessToken');

  return (
    <Routes>
      <Route index element={<Home/>} />
      <Route path='/careers' element={<Career/>} />
      {/* <Route path='/community' element={<Community />} /> */}
      <Route path='/about' element={<About/>} />
      <Route path='/contact' element={<Contact/>} />
      <Route path='/faq' element={<Faqs/>} />
      <Route path='/team' element={<Team/>} />
      <Route path='/blog' element={<Blog />} />
      <Route path='/communitypost' element={<Community />} />
      <Route path='/communitypost/:postId' element={<PostDetails />} />
      <Route path='/community/login' element={<ComLogin />} />
      <Route path='/community/addPosts' element={<AddPosts />} />
      {/* <Route path='*' element={<ProtectedRoute />} /> */}
      <Route path='/terms_policy' element={<TermsServices />} />
      <Route path='/alcohol' element={<Alcohol />} />
      <Route path='/careers/job' element={<JobApplication />} />
      <Route path='/newsletter' element={<NewsLetter/>} />
      {/* <Route path="*" element={<NotFound />} /> */}
    </Routes>
  )
}

export default CreateRoute;