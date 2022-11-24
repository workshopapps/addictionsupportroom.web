import React from 'react'

const Input = ({type, placeholder, id, icon}) => {
  return (
    <div className='flex w-full'>
        <input className='p-2 border-[2px] rounded-[4px] w-full' type={type} placeholder={placeholder}  id={id}/>
        <div className='rounded-[50%] border-[2px] p-2 ml-2'>
            <img  src={icon} alt="tel" />
        </div>
    </div>
  )
}

export default Input