from fastapi import APIRouter, HTTPException
from .crud import get_all_blogs, get_detail_blog

router = APIRouter()



@router.get('/')
def all_blogs():
    '''
    This endpoint is for getting all the blogs related to health from a blog site api 
    
    NOTE: this site is always updating their data that's why I'm not storing it in the database 
    '''
    result = get_all_blogs()
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail='Couldn\'t reach the site endpoint')


@router.get('/{blog_id}')
def a_blog(blog_id: int):
    '''
    This endpoint is for getting a particular blog from a blog site api 
    '''

    result = get_detail_blog(blog_id)
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail=f'There\'s no blog with id of {blog_id}')


