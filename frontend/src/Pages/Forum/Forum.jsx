import React from 'react'
import Download from '../../Components/Download/Download'
import Community from '../../Components/Froum/Community'
import HashTag from '../../Components/Froum/HashTag'
import PostFeed from '../../Components/Froum/PostFeed'
import PostInput from '../../Components/Froum/PostInput'
import { ForumHash, ForumCommunity, postFeed, posts } from "../../Data/Forum";

const Forum = () => {
  return (
    <div>
        <p className='font-[700] text-[40px] text-center mt-[30px] text-blue mb-[20px] '>Forum</p>
        <section className='block laptop:flex laptop:flex-rol justify-between mx-auto w-[90%]'>
            <div className=' laptop:w-[30%]'>
                <HashTag ForumHash={ForumHash}/>
                <Community ForumCommunity={ForumCommunity} />
            </div>
            <div className=' laptop:w-[65%] '>
                <PostInput postFeed={postFeed} />
                <PostFeed posts={posts} />
            </div>
        </section>
        <div className='mx-auto mt-20 mb-10 max-w-[1300px]'>
          <Download />
        </div>
        <br />
        <br />
    </div>
  )
}

export default Forum