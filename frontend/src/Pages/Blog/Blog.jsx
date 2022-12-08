import React, { useState, useEffect } from "react";
import axios from "axios";

import BlogPost from "../../Components/BLog/BlogPost";
import Download from "../../Components/Download/Download";
import { motion } from "framer-motion";
import BlogPaignation from "../../Components/BLog/BlogPaignation";

const Forum = () => {
  const [blogs, setBlogs] = useState([]);
  const [loading, setLoading] = useState(false);
  const [currentPage, setCurrentPage] = useState(1);
  const [postsPerPage] = useState(8);

  useEffect(() => {
    const fetchPosts = async () => {
      setLoading(true);
      const res = await axios.get("https://soberpal.hng.tech/api/blog/");
      setBlogs(res.data);
      setLoading(false);
    };

    fetchPosts();
  }, []);

  // Get current post
  const indexOfLastPost = currentPage * postsPerPage;
  const indexOfFirstPost = indexOfLastPost - postsPerPage;
  const currentPosts = blogs.slice(indexOfFirstPost, indexOfLastPost);

  //change page
  const paginate = (pageNumber) => setCurrentPage(pageNumber);

  return (
    <div>
      <motion.div
        whileInView={{ y: [100, 50], opacity: [0, 0, 1] }}
        transition={{ duration: 0.7 }}
      >
        <p className="font-[700] text-[30px] text-center mt-[30px] text-blue ">
          Blog
        </p>
        <p className="font-[700] text-[36px] laptop:text-[64px] text-center text-[black] mb-[10px] ">
          Addiction Insights
        </p>
        <p className="text-[16px] mx-auto w-[90%] tablet:w-[70%] laptop:w-[600px] tablet:text-[20px] text-center text-[black] mb-[20px] ">
          We help improve your self awareness by providing various <br />
          insights on your health.
        </p>
      </motion.div>

      {/* Blogs  */}
      <div className="my-20 ">
        <BlogPost loading={loading} blogs={currentPosts} />
        <BlogPaignation
          postsPerPage={postsPerPage}
          loading={loading}
          currentPage={currentPage}
          totalPosts={blogs.length}
          paginate={paginate}
        />
      </div>

      <section className="block laptop:flex laptop:flex-rol justify-between mx-auto w-[90%]"></section>
      <div className="w-full mb-[50px] mt-[90px] tablet:w-[70%] max-w-[1000px] mx-auto">
        <Download />
      </div>
      <br />
      <br />
    </div>
  );
};

export default Forum;
