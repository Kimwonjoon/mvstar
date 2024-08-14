import pandas as pd
import os
import requests
import math
import time
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
# MAKE JSON
def mkjson(pg = 1, dt = 2015, sleep_time = 1):
    dic = req(pg, dt) # 첫번째 10개 데이터 저장
    cnt = math.ceil(dic['movieListResult']['totCnt'] / 10) # 몇번 돌아야 하는가
    # 첫번째는 저장했으니 두번째부터
    for i in range(2,cnt+1):
        time.sleep(sleep_time) # 쉬었다가~
        data = req(i, dt) # 2번째 페이지부터 쭉쭉
        mvli = dic['movieListResult']['movieList'] # 영화 목록
        dic['movieListResult']['movieList'].extend(mvli) # 이미 있던 곳에 extend로 추가
    return dic
# SAVE_JSON
def save_movies(pg = 1, dt = 2015, sleep_time = 1):
    dir_path = f'/home/kimpass189/data/movies/year={dt}'
    # 폴더가 없는 경우만
    if not os.path.isdir(dir_path):
        # 디렉토리 생성
        os.makedirs(dir_path) # 경로 싹 생성
        result_dic = mkjson(pg, dt)
        with open(dir_path+'/data.json', 'w') as f: # Json 형태로 저장
            json.dump(result_dic, f)
    print("DONE!")
