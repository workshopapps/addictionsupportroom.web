import React from 'react'
import Button from "../../UI/Button"

const CardDownload = () => {
  return (
    <div className='block tablet:flex max-w-[1300px] mx-auto justify-between mb-12 w-[90%]'>
        <div>
            <p className='text-[28px] tablet:text-[28px] text-center laptop:text-[32px] font-[500] text-blue'>Download the Soberpal app</p>
            <p className='text-[18px] tablet:text-[18px] text-center laptop:text-[20px] text-[#575757]'>Join over 200+ people already growing with Soberpal.</p>
        </div>
        <div className='flex items-center justify-center mt-16 tablet:mt-0 '>
            <Button text="Download app" />
        </div>
    </div>
  )
}

export default CardDownload