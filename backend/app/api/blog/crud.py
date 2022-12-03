import requests


def clean_data(data):
    cleaned_data = data.replace("\r\n", '').replace('<ul><li>', '').replace('\r', '').replace('\n', '').replace('<ul>', '').replace('<li>', '')
    return cleaned_data


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
                'body': clean_data(container.get('content')),
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
        x = container.get('id')
        if x == blog_id:
            id = container.get('id'),
            title = container.get('title'),
            body = container.get('body'),
            imageURL = container.get('imageURL'),
            origin_blog = container.get('origin_blog')

            try:
                new_id = id[0]
                new_title = title[0]
                new_body = clean_data(body[0])
                new_imageURL = imageURL[0]
                new_origin_blog = origin_blog
            except:
                return None

            return {
                'id': new_id,
                'title': new_title,
                'body': new_body,
                'imageURL': new_imageURL,
                'origin_blog': new_origin_blog
            }
    return None
