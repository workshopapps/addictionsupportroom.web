import React from 'react'
import Input from '../../UI/Input'
import Telegram from "../../assets/telegram.svg"


const PostFeed = ({posts}) => {
  return (
    <div className='laptop:bg-[#FAFAFA] laptop:p-5 mt-[40px] laptop:border-[2px] rounded-[16px]'>
      {posts?.map((item, index) => (
        <div className='mb-16' key={index}>
          <div className='flex items-between'>
            <img className='h-[80px] w--[80px] tablet:h-[100px] tablet:w-[100px]' src={item.img} alt='img'/> 
            <div className='ml-3 tablet:ml-5 laptop:ml-8 pt-0 flex justify-between flex-col '>
              <p className='font-[700] text-[20px] tablet:text-[24px] laptop:text-[32px]'>{item.community}</p>
              <div  className='flex items-center '>
                <img className='h-[44px] tablet:h-[48px]  tablet:w-[48px]' src={item.avatar} alt="img" />
                <div className='flex flex-wrap'>
                  <span className='ml-2 font-[500] text-[#252525] text-[18px] laptop:text-[20px] '>{item.name}</span>
                  <span className='ml-2 text-[#252525]text-[16px] laptop:text-[18px]'>{item.duration}</span>
                </div>
              </div>
            </div>
          </div>
          <p className='font-[500] mt-8 text-[18px] tablet:text-[20px]'>{item.post}</p>
          {item?.hashs?.map((item, index) => (
            <div className='text-blue mt-2 flex flex-wrap gap-x-3 w-[80%] max-w-[360px] ' key={index}>
              <span className=' cursor-pointer'>{item.hash1}</span>
              <span className=' cursor-pointer'>{item.hash2}</span>
              <span className=' cursor-pointer'>{item.hash3}</span>
            </div>
          ))}
          
          <div className='flex mb-3 mt-2 '>
            <div className='flex flex-col  text-blue mt-2' >
              <img className='cursor-pointer' src={item?.imgPost[0]?.img1} alt="gg" />
            </div>
            <div className='flex flex-col text-blue mt-2' >
              <img className='cursor-pointer' src={item?.imgPost[1]?.img2} alt="g" />
              <img className='cursor-pointer' src={item?.imgPost[2]?.img3} alt="g" />
            </div>
          </div>
          <Input
              type ="text"
              placeholder="Post something to everyone"
              id="post"
              icon={Telegram}
          />

          {item.replies?.map((item, index) => (
            <div key={index}>
              <p className='my-3 text-[18px] tablet:text-[20px] font-[500]'>Replies to post (1)</p>
              <div className='flex items-center'>
                <img className='h-[48px] w-[48px] font-[500]' src={item.avatar} alt="a" />
                <div className='ml-4 flex flex-col justify-between'>
                  <p className='font-[500] tablet:text-[20px]' >{item.name}<span className='ml-3 text-[#3E3E3E] font-[400] text-[16px] '>{item.time}</span></p>
                  <p className='text-[16px] tablet:text-[20px] text-[#3E3E3E]'>{item.reply}</p>
                </div>
              </div>
            </div>
          ))}
        </div>
      ))}
    </div>
  )
}

export default PostFeed