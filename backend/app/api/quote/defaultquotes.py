from db.models import Quote
from sqlalchemy.orm import Session
from api import deps
from fastapi import Depends

def default_quotes(db: Session = Depends(deps.get_db)):
    new_quote = Quote(mood="happy", quote="don't worry.")
    new_quote2 = Quote(mood="happy", quote="be happy.")
    new_quote3 = Quote(mood="happy", quote="be happy.")
    new_quote = Quote(mood="anxious", quote="The Lord is your strength and your stronghold.")
    db.add(new_quote)
    db.add(new_quote2)
    db.add(new_quote3)
    Session.commit(db)

