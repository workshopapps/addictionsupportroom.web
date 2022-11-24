import React, { useState } from 'react'
import Telegram from "../../assets/telegram.svg"
import avatart from "../../assets/Ellipse.png"
import Input from '../../UI/Input'

const PostInput = ({postFeed}) => {
  const [disabled, setDisable] = useState(true)

  const handleChange = (e) => {
    if (e.target.value.length >= 2) {
      setDisable(false)
    }
  }

  return (
    <div className='p-2 tablet:p-4 bg-[#FAFAFA] border-[2px] rounded-[16px]'>
      <div className='flex'>
        <img src={avatart} alt="ff" className='h-[65px] w-[65px] tablet:w-[85px] tablet:h-[85px] ' />
        <div className='w-full ml-3  tablet:ml-[16px]'>
          <form>
            {/* <Input
              type ="text"
              placeholder="Post something to everyone"
              id="post"
              icon={Telegram}
            /> */}

              <div className='flex w-full'>
                <input 
                  className='p-2 border-[2px] rounded-[4px] w-full' 
                  type="text"
                  placeholder="post"
                  onChange={handleChange}  
                  // id={id}
                  // value=""
                />
                <button 
                  className='post-btn rounded-[50%] bg-blue cursor-pointer border-[2px] p-2 ml-2'
                  disabled="true"
                >
                  {/* button */}
                    <img className='' src={Telegram} alt="tel" />
                </button>
            </div>
          </form>
          <div className='hidden tablet:flex mt-4 justify-between'>
            {postFeed?.map((item) => (
              <div key={item.name} className=" cursor-pointer flex w-full max-w-[524px] items-center ">
                <img className='w-[20px] h-[20px] ' src={item.img} alt="img" />
                <span className='text-blue pl-1 laptop:pl-2  tablet:text-[14px] text-[16px]'>{item.name}</span>
              </div>
            ))}
          </div>
        </div>
        
      </div>
      <div className='tablet:hidden mt-4 w-full max-w-[524px] flex flex-wrap justify-between'>
            {postFeed?.map((item) => (
              <div key={item.name} className="flex  ">
                <img className='w-[20px] h-[20px] ' src={item.img} alt="img" />
                <span className='text-blue pl-2'>{item.name}</span>
              </div>
            ))}
          </div>
    </div>
  )
}

export default PostInput