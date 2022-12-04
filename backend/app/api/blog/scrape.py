import requests



def scrape():
    try:
        response = requests.get('https://saurav.tech/NewsAPI/top-headlines/category/health/in.json')
        res_obj = {**response.json()}
        articles = res_obj['articles']
        return {
            'message': 'Successful',
            'status': 200,
            'response': articles
        }
    except:
        return {
            'message': 'Page not found',
            'status': 404
        }