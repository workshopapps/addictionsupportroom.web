import React from 'react'

const HashTag = ({ForumHash}) => {
  return (
    <div>
      <div className=' hidden laptop:block laptop:bg-[#FAFAFA] border-[2px] rounded-[16px]'>
        <p className='text-[28px] font-[700] text-[#3E3E3E] py-3 text-center px-2 '>{ForumHash.header}</p>
        {ForumHash.tags?.map((item, index) => (
          <div key={index}>
            <div className='border-y-2 p-2'>
              <p className='text-blue font-[500] text-[20px] cursor-pointer'>{item.hash}</p>
              <p className='text-[#4F4F4F] text-[20px]  cursor-pointer'>{item.postCount}</p>
            </div>
          </div>
        ))}
      </div>

      <div>
      <div className='block laptop:hidden'>
        <p className='text-[20px] font-[700] text-[#3E3E3E] py-3 px-2 '>{ForumHash.header}</p>
        {ForumHash.tags?.map((item, index) => (
          <div key={index}>
            <div className=' p-2 flex justify-between  cursor-pointer'>
              <p className='text-blue font-[500] text-[16px] '>{item.hash}</p>
              <p className='text-[#4F4F4F] text-[16px] '>{item.postCount}</p>
            </div>
          </div>
        ))}
      </div>
      </div>
    </div>
  )
}

export default HashTag