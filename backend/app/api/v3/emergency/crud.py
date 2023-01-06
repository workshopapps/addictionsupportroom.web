from datetime import datetime
from db.models import Emergency, User
from datetime import datetime
from sqlalchemy.orm.session import Session




def find_user(username, db):
    """
    This function returns a user from the User table
    """
    user = db.query(User).filter(User.username==username).first()

    if user is None:
        new_user = User(username="lion", avatar="lion", hashed_password="lion")
        db.add(new_user)
        db.commit()

        find_user = db.query(User).filter(User.username=="lion").first()
        dict = {**find_user.__dict__}

        db.delete(new_user)
        db.commit()
    
    else:
        dict = {**user.__dict__}
    
    return {
            "username": dict["username"],
            "avatar": dict["avatar"],
            "id": dict["id"]
        }


def new_emergency(id, username, avatar, db):
    """
    This function adds an emergency to the Emergency table
    """

    emergency = Emergency(id=id, name=username, avatar=avatar, created_at=datetime.utcnow())
    db.add(emergency)
    db.commit()

    # #to delete, since this is still testing phase
    # db.delete(emergency)
    # db.commit()

    return "done"


def get_current_emergency(db: Session):
    emergency = db.query(Emergency).all()

    return emergency
