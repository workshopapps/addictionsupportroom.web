import React from 'react'
import { useParams } from 'react-router-dom'
import useFetch from '../../APIData/userFetch';
import messageText from "../../assets/message-text.png";



const PostDetails = () => {
  const { postId } = useParams();
  const { data: post, isPending, error } = useFetch("https://soberpal.hng.tech/api/forum/" + postId)

  return (
    <div>
      { error && <div className='text-blue text-[24px] font-[500] text-center'>{ error}</div>}
      { isPending && <div className='text-blue text-[24px] font-[500] text-center'>Loading...</div>}  
      { post && (
        <section>
          <p>Post</p>
          <div className="w-[90%] mx-auto">
          <div  className="bg-white w-full my-5 p-5 rounded-lg">
            <div className="flex gap-3">
              <img
                className="w-[50px] h-[50px] border-2 border-[black] rounded-full"
                src={post.user.avatar}
                alt="avatar"
              />
              <div className="flex flex-col justify-between">
                <p className="font-[500]">{post.user.username}</p>
                <p className="text-[12px]">{post.date_posted}</p>
              </div>
            </div>
            <p className="mt-5">{post.message}</p>
            <div className="flex gap-2 mt-3 items-center">
              <img
                className="w-[20px] h-[20px]"
                src={messageText}
                alt="message"
              />
              <p>comment</p>
            </div>
          </div>
    </div>
        </section>
      )}
    </div>
  )
}

export default PostDetails