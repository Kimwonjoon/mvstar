# mvstar
# Usage
```bash
$ pytest -s
================================================= test session starts ==================================================
platform linux -- Python 3.11.9, pytest-8.3.2, pluggy-1.5.0
rootdir: /home/kimpass189/code/mvstar
configfile: pyproject.toml
plugins: cov-5.0.0
collected 2 items

tests/test_call.py !!!데이터가 이미 존재합니다!!! : /home/kimpass189/data/movies/year=2015/data.json
!!!데이터가 이미 존재합니다!!! : /home/kimpass189/data/movies/year=2016/data.json
!!!데이터가 이미 존재합니다!!! : /home/kimpass189/data/movies/year=2017/data.json
!!!데이터가 이미 존재합니다!!! : /home/kimpass189/data/movies/year=2018/data.json
!!!데이터가 이미 존재합니다!!! : /home/kimpass189/data/movies/year=2019/data.json
!!!데이터가 이미 존재합니다!!! : /home/kimpass189/data/movies/year=2020/data.json
!!!데이터가 이미 존재합니다!!! : /home/kimpass189/data/movies/year=2021/data.json
.!!!데이터가 이미 존재합니다!!! : /home/kimpass189/data/movies/movieinfo/year=2015/data.json
100%|███████████████████████████████████████████████████████████████████████████████| 1575/1575 [12:37<00:00,  2.08it/s]
 11%|█████████▏                                                                      | 203/1769 [01:54<14:46,  1.77it/s]```
***
# Result
```bash
$ tree ~/data/movies/movieinfo
.
├── year=2015
│   └── data.json
└── year=2016
    └── data.json
```
***
# Error!!
## 하루 이용량 3000회 초과로 인해 하루에 1년치만 정상 저장 가능
```bash
$ pytest -s
======================================================= FAILURES =======================================================
______________________________________________________ test_info _______________________________________________________

    def test_info():
        for i in range(2015 ,2022):
>           r = read_data(dt = i, sleep_time = 0.1)

tests/test_call.py:10:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

dt = 2017, sleep_time = 0.1

    def read_data(dt = 2015, sleep_time = 1):
        file_path = f'/home/kimpass189/data/movies/movieinfo/year={dt}/data.json'
        # 파일이 있다면?
        if os.path.isfile(file_path):
            print(f"!!!데이터가 이미 존재합니다!!! : {file_path}")
            return True
        # 결과 저장 장소
        result = []
        # 파일 읽기
        with open(f"/home/kimpass189/data/movies/year={dt}/data.json", "r") as st_json:
            data_js = json.load(st_json)
        for dic in tqdm(data_js):
            time.sleep(sleep_time)
            mvcd = dic['movieCd']
            data = req(mvcd)
>           ap_dt = data['movieInfoResult']['movieInfo']
E           KeyError: 'movieInfoResult'

src/mvstar/mvinfo.py:45: KeyError
=============================================== short test summary info ================================================
FAILED tests/test_call.py::test_info - KeyError: 'movieInfoResult'
======================================= 1 failed, 1 passed in 872.98s (0:14:32) ========================================
```
## 키를 다 쓴 경우
```
{'faultInfo': {'message': '키의 하루 이용량을 초과하였습니다.', 'errorCode': '320011'}}
```
