from .scrape import scrape

def get_all_blogs():
    data = scrape()
    if data.get('status') == 200:
        result = []
        for index, item in enumerate(data.get('articles')):
            container = data.get('articles')[index]
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
        
    elif data.get('status') == 404:
        return None

