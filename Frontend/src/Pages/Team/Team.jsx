import React from 'react'
import './Team.css'
import TeamData from "../../Data/TeamData";
import Button from "../../UI/Button";
import TeamImg from '../../assets/team.png'
import TeamImgmobile from '../../assets/team-mobile.png'
import { AiOutlineClockCircle } from 'react-icons/ai';
import { AiOutlineDollar } from 'react-icons/ai';


const Team = () => {
    const download = 'Download app'
  return (

    /* team--container-----containing everything in the team page */
    <div className="team__container">

        {/* team---text---contents */}
      <div className="team">
        <div className="team__text">
            <span>The team</span>
            <h1>Meet the team behind Soberpal</h1>
            <p>We’re a small team that loves to create great experiences and make meaningful 
                connections between builders and customers. Join our remote ream!</p>
        </div>

        {/* different team images */}
        <div className="team__img">
            {/* mapped through my data file to access the images and informations */}
            {TeamData.map((data) => (
                <div className="team-info">
                    <img src={data.avatar} alt="" />
                    <h4>{data.name}</h4>
                    <p>{data.designation}</p>
                </div>
            ))}

            
        </div>
      </div>

      {/* team positions being looked for */}
      <div className="Team__position">
            <span>Open positions</span>
            <h2>We’re looking for talented people</h2>
            <p>We’re a 100% remote team spread all across the world. Join us!</p>
            <img src={TeamImg} alt="" id='teamImg'/>
            <img src={TeamImgmobile} alt="" id='teamImgmobile'/>

                {/* roles for team-positions */}
            <div className="team__position__roles">

                {/* the design roles */}
                <div className="design">
                    <h3 className='role__title'>Design</h3>
                    <div className="product__designer">
                        <h3 className='role'>Product Designer</h3>
                        <p>We’re looking for a mid-level product designer to join our team.</p>
                        <div className="role__desc__icons">
                            <span><AiOutlineClockCircle/> Full time</span>
                            <span><AiOutlineDollar/> 20k - 30k</span>
                        </div>
                        
                    </div>
                    <div className="product__designer">
                        <h3 className='role'>Product Designer</h3>
                        <p>We’re looking for a mid-level product designer to join our team.</p>
                        <div className="role__desc__icons">
                            <span><AiOutlineClockCircle/> Full time</span>
                            <span><AiOutlineDollar/> 40k - 60k</span>
                        </div>
                        
                    </div>
                </div>

                {/* software development roles */}
                <div className="software__development">
                    <h3 className='role__title'>Software Development</h3>

                    {/* frontend-development role under software development */}
                    <div className="frontend__developer">
                        <h3 className='role'>Frontend developer</h3>
                        <p>We’re looking for an experienced frontend 
                            developer to join our team.</p>
                        <div className="role__desc__icons">
                            <span><AiOutlineClockCircle/> Full time</span>
                            <span><AiOutlineDollar/> 80k - 100k</span>
                        </div>
                        
                    </div>
                </div>
            </div>
      </div>

        {/* download app section */}
      <div className="team__download-app">
        <div className="team__download-app-text">
          <h3>Download the Soberpal app</h3>
          <p className='team__p download__p'>Join over 200+ people already growing with Soberpal.</p>
        </div>

        {/* download button to download soberpal */}
        <div className="team__download-app-btn">
        <Button text={download} id='btn'/>
        </div>
      </div>
    </div>
  )
}

export default Team