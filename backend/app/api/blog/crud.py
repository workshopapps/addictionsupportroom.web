from sqlalchemy.orm import Session
from . import models
import requests


def get_all_blogs():
    response = requests.get('https://saurav.tech/NewsAPI/top-headlines/category/health/in.json')
    res_obj = {**response.json()}
    articles = res_obj['articles']
    result = []
    for index, item in enumerate(articles):
        container = articles[index]
        key = container['source']
        if index == 0: 
            key['id'] = 1
        else:
            key['id'] = index + 1
        
        if not (type(key.get('id')) == int):
            pass
        elif not (type(container.get('title')) == str):
            pass
        elif not (type(container.get('content')) == str):
            pass
        elif not (type(container.get('urlToImage')) == str):
            pass
        elif not (type(container.get('url')) == str):
            pass
        else: 
            result.append({
                'id': key.get('id'),
                'title': container.get('title'),
                'body': container.get('content'),
                'imageURL': container.get('urlToImage'),
                'origin_blog': container.get('url')
            })
    return result


def get_detail_blog(blog_id: int):
    '''
    This endpoint is for the details of the blog and since the blog is using an api to get it data the endpoint will lea to the origin of a particular data

    **id** - this field is required
    '''
    result = get_all_blogs()
    for i, j in enumerate(result):
        container = result[i]
        key = container['source']
        if key['id'] == blog_id:

            id = key.get('id'),
            title = container.get('title'),
            body = container.get('content'),
            imageURL = container.get('urlToImage'),
            origin_blog = container.get('url')

            if (id == None) or (title == None) or (body == None) or (imageURL == None) or (origin_blog == None):
                return None
            else:
                return {
                    'id': id,
                    'title': title,
                    'body': body,
                    'imageURL': imageURL,
                    'origin_blog': origin_blog
                }
    return None