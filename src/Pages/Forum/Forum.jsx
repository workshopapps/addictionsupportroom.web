import React, { useState } from 'react'
import Download from '../../Components/Download/Download'
import Community from '../../Components/Froum/Community'
import HashTag from '../../Components/Froum/HashTag'
import PostFeed from '../../Components/Froum/PostFeed'
import PostInput from '../../Components/Froum/PostInput'
import { ForumHash, OurWivesposts, Beginnerposts, ForumCommunity, postFeed, posts, ImFree, Thinking } from "../../Data/Forum";

const Forum = () => {
  const [active, setActive ] = useState (posts)

  return (
    <div className="max-w-[1300px] w-[95%] mx-auto">
        <p className='font-[700] text-[40px] text-center mt-[30px] text-blue mb-[20px] '>Forum</p>
        <section className='block laptop:flex laptop:flex-rol justify-between mx-auto w-full'>
            <div className=' laptop:w-[30%]'>
                <HashTag ForumHash={ForumHash}/>
                <Community ForumCommunity={ForumCommunity} active={active} setActive={setActive} />
            </div>
            <div className=' laptop:w-[65%] '>
                <PostInput postFeed={postFeed} />
                {active === posts && <PostFeed posts={posts} /> }
                <div>
                  {active === ImFree &&
                    <div className='mt-10'>
                      <p className='text-[64px] font-[700]'>No posts yet</p>
                      <p className='text-[32px] '>Be the first to make a post</p>
                    </div>
                  }
                  {active === Thinking &&
                    <div className='mt-10'>
                      <p className='text-[64px] font-[700]'>No posts yet</p>
                      <p className='text-[32px] '>Be the first to make a post</p>
                    </div>
                  }
                  {active === Beginnerposts && <PostFeed posts={Beginnerposts}/> }
                  {active === OurWivesposts && <PostFeed posts={OurWivesposts} />}

                </div>
            </div>
        </section>
        <div className='mx-auto mt-20 mb-10'>
          <Download />
        </div>
        <br />
        </div>
  )
}

export default Forum;