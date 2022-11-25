import React from 'react'
import { ImFree, Thinking, OurWivesposts, Beginnerposts } from "../../Data/Forum";

import c1 from "../../assets/c1.png"
import c2 from "../../assets/c2.png"
import c3 from "../../assets/c3.png"
import c4 from "../../assets/c4.png"


  const Community = ({ForumCommunity, setActive, active}) => {
    return (
      <div>
        <div className=' hidden laptop:block bg-[#FAFAFA] mt-20 border-[2px] rounded-[16px]'>
          <p className='text-[28px] font-[700] text-[#3E3E3E] py-3 text-center '>{ForumCommunity.header}</p>
          <div 
            onClick={() => setActive(Beginnerposts)}
            className={ ` hover:bg-[#B2B2B2] border-y-2 py-2 px-4 gap-5 flex cursor-pointer hover:scale-105 transition ease-in-out delay-100 
              ${active === Beginnerposts ?  "bg-[#B2B2B2]" :" bg-[#FAFAFA]" }`}
          >
            <img src={c1} alt="img" className='w-[80px] h-[80px] ' />
            <div className=' my-auto  '>
              <p className='text-[#3E3E3E] text-[15px] '>PUBLIC COMMUNITY</p>
              <p className='text-[#252525] text-[18px] font-[500] '>Beginner</p>
              <p className='text-[#3E3E3E] text-[16px] '>23 members</p>
            </div>
          </div>
  
          <div 
            onClick={() => setActive(ImFree)}
            className={ ` hover:bg-[#B2B2B2] border-y-2 py-2 px-4 gap-5 flex cursor-pointer hover:scale-105 transition ease-in-out delay-100
              ${active === ImFree ?  "bg-[#B2B2B2]" :" bg-[#FAFAFA]" }`}
          >
            <img src={c2} alt="img" className='w-[80px] h-[80px] ' />
            <div className=' my-auto'>
              <p className='text-[#3E3E3E] text-[15px] '>PUBLIC COMMUNITY</p>
              <p className='text-[#252525] text-[18px] font-[500] '>I'm free</p>
              <p className='text-[#3E3E3E] text-[16px] '>23 members</p>
            </div>
          </div>
  
          <div 
            onClick={() => setActive(Thinking)}
            className={ ` hover:bg-[#B2B2B2] border-y-2 py-2 px-4 gap-5 flex cursor-pointer hover:scale-105 transition ease-in-out delay-100
              ${active === Thinking ?  "bg-[#B2B2B2]" :" bg-[#FAFAFA]" }`}
          >
            <img src={c3} alt="img" className='w-[80px] h-[80px] ' />
            <div className=' my-auto'>
              <p className='text-[#3E3E3E] text-[15px] '>PUBLIC COMMUNITY</p>
              <p className='text-[#252525] text-[18px] font-[500] '>Thinking</p>
              <p className='text-[#3E3E3E] text-[16px] '>23 members</p>
            </div>
          </div>
  
          <div 
            onClick={() => setActive(OurWivesposts)}
            className={ ` hover:bg-[#B2B2B2] border-y-2 py-2 px-4 gap-5 flex cursor-pointer hover:scale-105 transition ease-in-out delay-100
              ${active === OurWivesposts ?  "bg-[#B2B2B2]" :" bg-[#FAFAFA]" }`}
          >
            <img src={c4} alt="img" className='w-[80px] h-[80px] ' />
            <div className=' my-auto'>
              <p className='text-[#3E3E3E] text-[15px] '>PUBLIC COMMUNITY</p>
              <p className='text-[#252525] text-[18px] font-[500] '>Our wives</p>
              <p className='text-[#3E3E3E] text-[16px] '>23 members</p>
            </div>
          </div>
  
        </div>     
  
        <div className=' flex laptop:hidden laptop:bg-[#FAFAFA] my-6 justify-between'>
          <p className='text-[20px] font-[700] text-[#3E3E3E] py-3'>{ForumCommunity.header}</p>
          <select name="forum" id="forum " className="border-[2px] rounded-[16px] p-2">
          {ForumCommunity.tags?.map((item, index) => (
              <option key={index} className='text-[#252525] text-[18px] font-[500]' value={item.level} >{item.level}</option>
          ))}
          </select>
            {/* <div  className="border-[2px] rounded-[16px] p-2 no-list">
              <li  className='text-[#252525] text-[18px] font-[500]' >All</li>
              <div className='no-list mt-1'>
                <li  className='text-[#252525] text-[18px] font-[500]' >Beginner</li>
                <li  className='text-[#252525] text-[18px] font-[500]' >I'm free</li>
                <li  className='text-[#252525] text-[18px] font-[500]' >Thinking</li>
                <li  className='text-[#252525] text-[18px] font-[500]' >Our wives</li>
              </div>
            </div> */}
        </div>
      </div>
    )   
}

export default Community