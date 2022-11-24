import random

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from api import deps
from db.models import Quote

router = APIRouter()

class QuoteRequest(BaseModel):
    mood: str


@router.post("/")
def get_quote(data: QuoteRequest, db: Session = Depends(deps.get_db)):
    mood = data.mood

    #temporarily create records in Quote table
    new_quote = Quote(mood="happy", quote="don't worry.")
    new_quote2 = Quote(mood="happy", quote="be happy.")
    db.add(new_quote)
    db.add(new_quote2)
    Session.commit(db)

    quotes = list(db.query(Quote).filter(Quote.mood==mood).all())
    quote = random.choice(quotes)

    formatted_quote = quote.quote

    return {
        "quote": formatted_quote
    }