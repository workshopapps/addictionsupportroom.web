import React from 'react'
import {GrClose} from 'react-icons/gr'
import {  Link } from 'react-router-dom'
import { navbarList } from '../../Data/navbar'


const MobileNav = ({setIsOpen}) => {
  return (
    <div className='fixed bg-blue z-50 w-[100%] h-[100rem] right-0 top-0 '>
        <button
            className='absolute right-[6%] top-[1.5%] text-white text-[24px]'
            onClick={() => setIsOpen(false)}
        >
            <GrClose/>
        </button>
          <ul className='mt-[60px]'>
            {navbarList.navList.map(({ page, link}) => 
              <>
              <Link 
                key={page} 
                to={link}
                onClick={() => setIsOpen(false)}
              >
                <li className='p-4 font-[700] mx-3 text-white'>{page}</li>
              </Link>
              </>
            )}
              <Link className="ml-5 w-full mx-auto" rel="noreferrer" href="https://appetize.io/app/q3qnqdo5ibklola6h5xlimn6rq?device=pixel4&osVersion=11.0&scale=75" target="_blank" >
                <button className="font-[500] p-4 bg-[white] text-blue mt-[30px] rounded-[16px] " >Download App</button>
              </Link>
          </ul>
    </div>
  )
}

export default MobileNav
