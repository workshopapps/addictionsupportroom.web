import React from 'react'

const Button = ({text, onClick}) => {
  return (
    <button 
        onClick={onClick}
        className='bg-blue py-[10px] px-[16px] rounded-[8px] text-white hover--effect '
    >
        {text}
    </button>
  )
}

export default Button