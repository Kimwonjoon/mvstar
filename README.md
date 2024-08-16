# mvstar
# Usage
```bash
$ pytest -s
================================================= test session starts ==================================================
platform linux -- Python 3.11.9, pytest-8.3.2, pluggy-1.5.0
rootdir: /home/kimpass189/code/mvstar
configfile: pyproject.toml
plugins: cov-5.0.0
collected 1 item

100%|█████████████████████████████████████████████████████████████████████████████████| 120/120 [00:42<00:00,  2.81it/s]
100%|█████████████████████████████████████████████████████████████████████████████████| 157/157 [01:00<00:00,  2.59it/s]
100%|█████████████████████████████████████████████████████████████████████████████████| 176/176 [01:03<00:00,  2.76it/s]
100%|█████████████████████████████████████████████████████████████████████████████████| 187/187 [01:04<00:00,  2.90it/s]
100%|█████████████████████████████████████████████████████████████████████████████████| 195/195 [01:15<00:00,  2.59it/s]
100%|█████████████████████████████████████████████████████████████████████████████████| 189/189 [01:05<00:00,  2.88it/s]
100%|█████████████████████████████████████████████████████████████████████████████████| 185/185 [01:10<00:00,  2.61it/s]
```
***
# Result
```bash
$ tree ~/data/movies
.
├── year=2015
│   └── data.json
├── year=2016
│   └── data.json
├── year=2017
│   └── data.json
├── year=2018
│   └── data.json
├── year=2019
│   └── data.json
├── year=2020
│   └── data.json
└── year=2021
    └── data.json
```
***
# If you already have the data
```bash
$ pytest -s
================================================= test session starts ==================================================
platform linux -- Python 3.11.9, pytest-8.3.2, pluggy-1.5.0
rootdir: /home/kimpass189/code/mvstar
configfile: pyproject.toml
plugins: cov-5.0.0
collected 1 item

tests/test_call.py !!!데이터가 이미 존재합니다!!! : /home/kimpass189/data/movies/year=2015/data.json
!!!데이터가 이미 존재합니다!!! : /home/kimpass189/data/movies/year=2016/data.json
!!!데이터가 이미 존재합니다!!! : /home/kimpass189/data/movies/year=2017/data.json
!!!데이터가 이미 존재합니다!!! : /home/kimpass189/data/movies/year=2018/data.json
!!!데이터가 이미 존재합니다!!! : /home/kimpass189/data/movies/year=2019/data.json
!!!데이터가 이미 존재합니다!!! : /home/kimpass189/data/movies/year=2020/data.json
!!!데이터가 이미 존재합니다!!! : /home/kimpass189/data/movies/year=2021/data.json
```
