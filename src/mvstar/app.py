import pandas as pd
import os
import requests
import math
import time
from tqdm import tqdm
# API_KEY
key = os.getenv('MOVIE_API_KEY')

# URL
def gen_url(pg = 1, dt = 2015):
    base_url = 'http://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json'
    url = f'{base_url}?key={key}&curPage={pg}&openStartDt={dt}&openEndDt={dt}'
    return url

# Load JSON
def req(pg = 1, dt = 2015):
    url = gen_url(pg, dt)
    res = requests.get(url)
    data = res.json()
    return data

# SAVE_JSON
def save_movies(data, file_path):
    # 디렉토리 생성
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(dir_path+'/data.json', 'w', encoding = "utf-8") as f: # Json 형태로 저장
        json.dump(data, f, indent = 4, ensure_ascii=False)
    print("DONE!")

# MAKE JSON
def mkjson(pg = 1, dt = 2015, sleep_time = 1):
    file_path = f'/home/kimpass189/data/movies/year={dt}/data.json'
    dic = req(pg, dt) # 첫번째 10개 데이터 저장
    #result = dic['movieListResult']['movieList']
    result = []
    cnt = math.ceil(dic['movieListResult']['totCnt'] / 10) # 몇번 돌아야 하는가
    # 첫번째는 저장했으니 두번째부터
    for i in tqdm(range(1,cnt+1)):
        time.sleep(sleep_time) # 쉬었다가~
        data = req(i, dt) # 1번째 페이지부터 쭉쭉
        mvli = data['movieListResult']['movieList'] # 영화 목록
        result.extend(mvli) # 이미 있던 곳에 extend로 추가
    save_movies(dic, file_path)
    return True
