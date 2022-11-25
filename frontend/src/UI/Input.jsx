import React,{useState} from 'react'


const Input = ({type, placeholder, id, icon, value, onChange, }) => {
  const [disabled, setDisable] = useState(true)

  const handleChange = (e) => {
    if (e.target.value.length >= 1) {
      setDisable(false)
    } else {
      setDisable(true)
    }
  }
  
  return (
    <div className='flex w-full'>
      <input 
        className='p-2 border-[2px] rounded-[4px] w-full outline-blue ' 
        type={type}
        placeholder={placeholder}  
        id={id}
        value={value}
        onChange={handleChange}  
      />
      <button 
        className={ ` hover:bg-[#B2B2B2] rounded-[50%]  border-[2px] p-2 ml-2 transition ease-in-out delay-100
        ${disabled ?  "opacity-50 cursor-not-allowed bg-[#B2B2B2]" :" bg-[#FAFAFA] cursor-pointer" }`}
        type="submit"
      >
          <img className='' src={icon} alt="tel" />
      </button>
    </div>
  )
}

export default Input