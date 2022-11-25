import React,{useState} from 'react'

const Modal = ({setShowModal}) => {
    const [disabled, setDisable] = useState(true)

    const handleChange = (e) => {
      if (e.target.value.length >= 1) {
        setDisable(false)
      } else {
        setDisable(true)
      }
    }
  return (
    <>
        <div
            className="justify-center items-center flex overflow-x-hidden overflow-y-auto fixed inset-0 z-50 outline-none focus:outline-none"
          >
            <div className="relative w-[90%]  tablet:w-[70%]laptop:w-[60%]  my-6 mx-auto max-w-3xl ">
              {/*content*/}
              <div className="border-0 rounded-lg shadow-lg relative flex flex-col w-full bg-white outline-none focus:outline-none">
                {/*header*/}
                <div className="flex items-start justify-between p-5 border-b border-solid border-slate-200 rounded-t">
                  <h3 className="text-3xl font-semibold">
                    Write a post to the Community
                  </h3>
                  <button
                    className="p-1 ml-auto border-0 text-black  float-right text-3xl leading-none font-semibold outline-none focus:outline-none"
                    onClick={() => setShowModal(false)}
                  >
                    <span className="text-black h-6 w-6 text-2xl block outline-none focus:outline-none">
                      x
                    </span>
                  </button>
                </div>
                
                <div className='mt-10 m-[20px]'>
                <textarea 
                    className='p-2 border-[2px] rounded-[4px] outline-blue h-[300px] w-full' 
                    type="text"
                    placeholder="Post something to everyone" 
                    onChange={handleChange}  
                />
                <button 
                    className={ `mt-10 w-full hover:bg-[#B2B2B2]]  border-[2px] p-2 ml-2 transition ease-in-out delay-100
                    ${disabled ?  "opacity-50 cursor-not-allowed bg-[#B2B2B2]" :" bg-blue text-white cursor-pointer" }`}
                    type="submit"
                > 
                    Post                    
                </button>
                </div>
              </div>
            </div>
          </div>
          <div className="opacity-25 fixed inset-0 z-40 bg-black"></div>
    </>
  )
}

export default Modal