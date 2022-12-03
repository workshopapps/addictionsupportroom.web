from fastapi import APIRouter, HTTPException
from .crud import get_all_blogs

router = APIRouter()



@router.get('/')
def all_blogs():
    '''
    This endpoint is for getting all the blogs related to health froma blog site api 
    
    NOTE: this site is always updating their data that's why I'm not storing it in the database 
    '''
    result = get_all_blogs()
    if result:
        return result
    else:
        raise HTTPException(status_code=404,)


