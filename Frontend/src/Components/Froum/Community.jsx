import React from 'react'

const Community = ({ForumCommunity}) => {
  return (
    <div>
      <div className=' hidden laptop:block bg-[#FAFAFA] mt-20 border-[2px] rounded-[16px]'>
        <p className='text-[28px] font-[700] text-[#3E3E3E] py-3 text-center '>{ForumCommunity.header}</p>
        {ForumCommunity.tags?.map((item, index) => (
          <div key={index}>
            <div className='border-y-2 py-2 px-4 justify-between flex '>
              <img src={item.img} alt="img" className='w-[100px] h-[100px] ' />
              <div className=' my-auto '>
                <p className='text-[#3E3E3E] text-[16px] '>{item.coummunity}</p>
                <p className='text-[#252525] text-[18px] font-[500] '>{item.level}</p>
                <p className='text-[#3E3E3E] text-[16px] '>{item.members} members</p>
              </div>
            </div>
          </div>
        ))}
      </div>

      <div className=' flex laptop:hidden bg-[#FAFAFA] mt-6'>
        <p className='text-[20px] font-[700] text-[#3E3E3E] py-3'>{ForumCommunity.header}</p>
        <select name="forum" id="forum">
        {ForumCommunity.tags?.map((item, index) => (
            <option key={index} className='text-[#252525] text-[18px] font-[500]' value={item.level} >{item.level}</option>
        ))}
        </select>
      </div>
    </div>
  )
}

export default Community