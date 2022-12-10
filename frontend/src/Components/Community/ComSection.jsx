import React from 'react'

const ComSection = ({post}) => {
  return (
    <section className='w-full mx-auto mt-8 mb-16'>

        { post.post_comments.map((comment) => (
            <div key={comment.id} className="bg-white w-full rounded-lg">
            <hr className="bg-[#BBBBBB] h-[2px] mt-2 mb-3" />
            <div className="flex gap-3">
                <img
                className="w-[40px] h-[40px] border-2 border-[#BBBBBB] rounded-full"
                src={comment.owner.avatar}
                alt="avatar"
                />
                <div className="flex flex-col justify-between">
                <p className="font-[500] text-[14px]">{comment.owner.username}</p>
                <p className="text-[12px]">{comment.date_posted}</p>
                </div>
            </div>
            <p className="mt-3">{comment.comment}</p>
        </div>
        ))}
      <hr className="bg-[#BBBBBB] h-[2px] mt-2 mb-2" />

    </section>
  )
}

export default ComSection
