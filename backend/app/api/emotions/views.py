from fastapi import APIRouter
from .quotes import happy,confused,angry,sober,defeated
import random
router = APIRouter()



@router.post("/")
async def post_emotion(request):
	if request == "happy":
		return(happy[random.randint(0,2)])
	elif request == "sober":
		return(sober[random.randint(0,2)])
	elif request == "defeated":
		return(defeated[random.randint(0,2)])
	elif request == "angry":
		return(angry[random.randint(0,2)])
	else:
		return(confused[random.randint(0,2)])

