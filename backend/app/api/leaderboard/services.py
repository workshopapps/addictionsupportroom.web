# import schemas
# from db.models import Rank
# from sqlalchemy import select
# from sqlalchemy.orm import Session


# class RankingService:
#     # def __init__(self, session: AsyncSession = Depends(db_session)):
#     #     self.session = session

#     async def get_all_examples(self, db: Session) -> list[schemas.Ranking]:
#         ranks = db.query(Rank).all()

#         return ranks
    

#     def create_example(self, db: Session, data) -> Rank:
#         rank = Rank(**data.dict())
#         db.add(rank)
#         db.commit()
#         db.refresh(rank)

#         return rank
