import React from 'react'

const BlogPaignation = ({ currentPage, postsPerPage, totalPosts, paginate }) => {
  const pageNumbers = [];

  for(let i = 1; i <= Math.ceil(totalPosts / postsPerPage); i++){
    pageNumbers.push(i);
  }
  return (
    <div className='flex justify-end mt-20 py-5  max-w-[1300px] w-[90%] mx-auto'>
      <ul className=' flex  w-fit'>
        {pageNumbers.map(number => (
          <li key={number} className="">
            <a 
              onClick={() => paginate(number)}
              href='/#/blog/#' 
              className={
                currentPage === number
                    ? "px-3 py-2 rounded-md border-1 text-[18px] text-white font-[500] bg-blue m-2 border-[black]"
                    : "px-3 py-2 rounded-md border-1 text-[18px] text-black font-[500] m-2 border-[black]"
                }
              >
              {number}
            </a>
          </li>
        ))}
      </ul>
    </div>
  )
}

export default BlogPaignation