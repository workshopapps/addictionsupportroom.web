from sqlalchemy.orm.session import Session
from .schemas import PostBase, PostCommentBase
from db.models import ForumPost, ForumPostComment, User
from fastapi import HTTPException


class PostClass():
    '''
        This class handles all the Post CRUD operations
    '''

    def __init__(self, current_user: User) -> None:
        self.current_user = current_user

    def get_all_users(self, db: Session):
        users = db.query(User).all()
        return users

    def create_post(self, db: Session, request: PostBase):
        user = self.current_user
        new_post = ForumPost(
            message=request.message,
            user_username=user.username
        )
        db.add(new_post)
        db.commit()
        db.refresh(new_post)
        return new_post

    def get_all_post(self, db: Session):
        '''
            **Sample Response Data** :
                    [
                        {
                            "id": 1,
                            "message": "string",
                            "user": {
                                "id": 1,
                                "username": "henzyd",
                                "avatar": "http://www.example.com/image"
                            },
                            "post_comments": [
                                {
                                    "owner": {
                                        "id": 1,
                                        "username": "henzyd",
                                        "avatar": "http://www.example.com/image"
                                    },
                                    "origin_post": {
                                        "id": 1,
                                        "message": "string",
                                        "date_posted": "2022-12-07T13:16:04.325737"
                                    },
                                    "comment": "string",
                                    "date_posted": "2022-12-07T13:18:03.435170"
                                }
                            ],
                            "num_of_comments": 1,
                            "date_posted": "2022-12-07T13:16:04.325737"
                        }
                    ]
        '''
        posts = db.query(ForumPost).all()
        for post in posts:
            comment = db.query(ForumPostComment).filter(ForumPostComment.origin_post_id == post.id).all()
            post.post_comments = comment
            post.num_of_comments = f'{len(post.post_comments)} comments'
        return posts

    def get_post(self, db: Session, id: int):
        '''
            **Sample Response Data**:
                {
                    "id": 1,
                    "message": "string",
                    "user": {
                        "id": 1,
                        "username": "henzyd",
                        "avatar": "http://www.example.com/image"
                    },
                    "post_comments": [
                        {
                            "owner": {
                                "id": 1,
                                "username": "henzyd",
                                "avatar": "http://www.example.com/image"
                            },
                            "origin_post": {
                                "id": 1,
                                "message": "string",
                                "date_posted": "2022-12-07T13:16:04.325737"
                            },
                            "comment": "string",
                            "date_posted": "2022-12-07T13:18:03.435170"
                        }
                    ],
                    "num_of_comments": 1,
                    "date_posted": "2022-12-07T13:16:04.325737"
                }
        '''

        post = db.query(ForumPost).filter(ForumPost.id == id).first() #### BUG
        if post:
            comment = db.query(ForumPostComment).filter(ForumPostComment.origin_post_id == post.id).all()
            post.post_comments = comment
            post.num_of_comments = f'{len(post.post_comments)} comments'
            return post
        else:
            return None

    def delete_a_post(self, db: Session, id: int):
        post_by_user = db.query(ForumPost).filter(ForumPost.id == id).first()
        if post_by_user:
            if post_by_user.user.username == self.current_user.username:
                db.delete(post_by_user)
                db.commit()
            else:
                raise HTTPException(status_code=401, detail=f'This user is not allowed to delete this post')
        else:
            raise HTTPException(status_code=404, detail=f'Post of ID {id} does not exist')
        print(post_by_user)
        return post_by_user

    def create_post_comment(self, db: Session, request: PostCommentBase):
        post = db.query(ForumPost).filter(ForumPost.id == request.origin_post_id).first()
        if post:
            new_comment = ForumPostComment(
                owner_username=self.current_user.username,
                origin_post_id=request.origin_post_id,
                comment=request.comment
            )
            db.add(new_comment)
            db.commit()
            db.refresh(new_comment)
            return new_comment
        else:
            return None

    
