import React, {useState, useEffect} from "react";

const BlogPost = ({blogs, loading}) => {

  if (loading) {
    return <h2>Loading...</h2>
  }



  return (
    
    <div className="flex flex-wrap max-w-[1300px] w-[90%] mx-auto justify-between">
      
      {blogs?.map(({imageURL, title, body, origin_blog, id }) => (
        <div
          key={id} 
          className="flex mt-12 gap-5 mx-auto w-[90%] desktop:w-[45%] "
        >
          <img className="h-[180px] w-[180px]" src={imageURL} alt="c1" />
          <div>
            <p className="text-[20px] text-[black] font-[600] leading-8">
              {title}
            </p>
            <p className="text-[16px] tablet:text-[16px] ">{body}</p>
            <a href={origin_blog}  rel="noreferrer" target="_blank" className="text-[16px] text-blue">Read more ...</a>
          </div>
        </div>

      ))}

    </div>
  );
};

export default BlogPost;
