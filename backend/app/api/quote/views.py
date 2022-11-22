import random

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from api import deps
from db.models import Quote

from .defaultquotes import default_quotes



router = APIRouter()


class QuoteRequest(BaseModel):
    mood: str


@router.post("/")
def get_quote(data: QuoteRequest, db: Session = Depends(deps.get_db)):
    default_quotes(db)

    mood = data.mood

    quotes = list(db.query(Quote).filter(Quote.mood==mood).all())
    quote = random.choice(quotes)

    formatted_quote = quote.quote

    return {
        "quote": formatted_quote
    }