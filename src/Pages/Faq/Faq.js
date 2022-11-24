import React from 'react'
import './Faq.css'
import FaqData from "../../Data/FaqData";
import helpcenter from "../../assets/helpcenter.png";
import Button from "../../UI/Button";
import Input from '../../UI/Input';
/* import Button2 from "../../UI/Button2"; */


const Faq = () => {
  return (
    /* faq__container----contains everything in the faq page */

    <div className="faq__container">

      {/* the help center----containing the text and image */}
      <div className="faq__help-center">
        <div className="faq__help-center__text">
          <h1>Help centre</h1>
          <p className='faq__p'>Support that is always online.Get all the help you need about the product here.</p>
        </div>
        <div className="faq__help-center__img">
          <img src={helpcenter} alt="" />
        </div>

      </div>

      {/* the form in the faq page containing the input and button */}
      <div className="faq__form-question first__form">
        <h4 className='faq__form__title'>Have a question?</h4>

        {/* the form */}
        <form action="">
            
         <input type="email" name="" id="" placeholder='Enter your email adress'/>
           {/* the send button in the form */} 
          <Button text={FaqData.send} /> 
        </form>

      </div>

      <hr className='hr'/>

      {/* the faq section */}
      <div className="faq__section2">
        <h2>FAQs</h2>
        <p className='faq__p'>Everything you need to go through the journey of reducing your alcohol intake.  These are frequently asked questions bout the product. Dont find answer to your question?? send us amessage..</p>

        {/* faq questions and answer */}
        <div className="faq__questions-answer-section">
          <p>What is Soberpal?<span>+</span></p>
          <hr className='faq__border-bottom'/>

          <p>Can i be annoymous?<span>+</span></p>
          <hr className='faq__border-bottom'/>

          <p>Do i get a personal sponser?<span>+</span></p>
          <hr className='faq__border-bottom'/>
 
          <p>How does billing work<span>+</span></p>
          <hr className='faq__border-bottom'/>

          <p>How do I change my account email<span>+</span></p>
        </div>
      </div>

      
      {/* the form in the faq page containing the input and button */}
      <div className="faq__form-question">
        <h4 className='faq__form__title'>Have a question?</h4>
        {/* the form */}
        <form action="">
          <input type="email" name="" id="" placeholder='Enter your email adress'/>
           
          <Button text={FaqData.send} id='btn'/> 
        </form>

      </div>

      {/* download soberpal app */}
      <div className="faq__download-app">
        <div className="faq__download-app-text">
          <h3>Download the Soberpal app</h3>
          <p className='faq__p download__p'>Join over 200+ people already growing with Soberpal.</p>
        </div>
        <div className="faq__download-app-btn">
          {/* download button */}
        <Button text={FaqData.download} id='btn'/>
        </div>
      </div>
    </div>
  )
}

export default Faq