import React, {useState, useEffect} from "react";
import { motion } from "framer-motion";

const BlogPost = ({posts, loading}) => {

  // title, body, id, URl, urlLink 
  // console.log(post)

  if (loading) {
    return <h2>Loading...</h2>
  }



  return (
    
    <div className="flex flex-wrap max-w-[1300px] w-[90%] mx-auto justify-between">
      <motion.p 
         whileInView={{ y: [100, 50], opacity: [0, 0, 1] }}
         transition={{ duration: 0.7 }} 
        className="text-[28px] font-[500] my-10 text-center">This is just a dummy data... im yet to get an API endpoint from the backend developer</motion.p>
      {posts.blog.map(({img, title, body, id }) => (
        <motion.div
          whileInView={{ y: [100, 50], opacity: [0, 0, 1] }}
          transition={{ duration: 0.7 }} 
          key={id} 
          className="flex mt-12 gap-5 mx-auto w-[90%] laptop_l:w-[45%] "
        >
          <img className="h-[180px] w-[180px]" src={img} alt="c1" />
          <div>
            <p className="text-[22px] tablet:text-[24px] text-[black] font-[600] leading-8">
              {title}
            </p>
            <p className="text-[16px] tablet:text-[18px] font-[500] ">{body}</p>
            <p className="text-[16px] text-blue">Read more ...</p>
          </div>
        </motion.div>

      ))}

    </div>
  );
};

export default BlogPost;
