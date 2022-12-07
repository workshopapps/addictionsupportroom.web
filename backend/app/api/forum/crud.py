from db.db import get_db
from sqlalchemy.orm.session import Session
from .schemas import PostBase, PostCommentBase
from db.models import ForumPost, ForumPostComment, User


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
                                },
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
                                    "date_posted": "2022-12-07T13:18:34.120460"
                                }
                            ],
                            "date_posted": "2022-12-07T13:16:04.325737"
                        }
                    ]
        '''
        posts = db.query(ForumPost).all()
        for post in posts:
            comment = db.query(ForumPostComment).filter(ForumPostComment.origin_post_id == post.id).all()
            post.post_comments = comment
        return posts

    def get_post(self, db: Session, id: int):
        try:
            post = db.query(ForumPost).filter(ForumPost.id == id).first()
        except:
            return None
        comment = db.query(ForumPostComment).filter(ForumPostComment.origin_post_id == post.id).all()
        post.post_comments = comment
        return post

    def create_post_comment(self, db: Session, request: PostCommentBase):
        new_comment = ForumPostComment(
            owner_username=self.current_user.username,
            origin_post_id=request.origin_post_id,
            comment=request.comment
        )
        db.add(new_comment)
        db.commit()
        db.refresh(new_comment)
        return new_comment
