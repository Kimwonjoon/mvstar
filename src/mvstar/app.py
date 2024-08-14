import pandas as pd
import tqdm
import requests
import os
def gen_url(pg = 1, opdt = 2015, cldt = 2021):
    base_url = 'http://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json'
    key = os.getenv('MOVIE_API_KEY')
    url = f'{base_url}?key={key}&curPage={pg}&openStartDt={opdt}&openEndDt={cldt}'
    return url

def req(pg = 1, opdt = 2015, cldt = 2021):
    url = gen_url(pg, opdt, cldt)
    res = requests.get(url)
    data = res.json()
    return data
