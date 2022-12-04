import React from "react";

const BlogPost = ({blogs, loading}) => {

  if (loading) {
    return <h2 className="text-[20px] font-[600] text-center">Loading...</h2>
  }



  return (
    
    <div className="flex flex-wrap max-w-[1300px] w-[90%] mx-auto justify-between">
      
      { blogs?.map(({ imageURL, title, body, origin_blog, id }) => (
        <div Key={id} 
          className="block tablet:flex mt-12 gap-2 tablet:gap-5 mx-auto w-[95%] tablet:w-[90%] desktop:w-[45%] "
        >
          <img className="h-[150px] w-[100%] tablet:h-[140px] tablet:w-[150px] laptop:h-[150px] laptop:w-[160px] desktop:h-[150px] desktop:w-[150px] xl:h-[180px] xl:w-[180px]" src={imageURL} alt="c1" />
          <div>
            <p className="text-[16px] tablet:text-[19px] laptop:text-[20px] text-[black] font-[600] leading-5 tablet:leading-6 laptop:leading-8">
              {title}
            </p>
            <p className="hidden tablet:block text-[16px] tablet:text-[16px] "> {body.slice(0, 80)}...</p>
            <p className="tablet:hidden text-[14px] tablet:text-[16px] "> {body.slice(0, 50)}...</p>
            <a href={origin_blog}  rel="noreferrer" target="_blank" className="text-[16px] text-blue">Read more ...</a>
          </div>
        </div>

      ))}

    </div>
  );
};

export default BlogPost;
