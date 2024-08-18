# mvstar
# Usage
```bash
$ pytest -s
================================================= test session starts ==================================================
platform linux -- Python 3.11.9, pytest-8.3.2, pluggy-1.5.0
rootdir: /home/kimpass189/code/mvstar
configfile: pyproject.toml
plugins: cov-5.0.0
collected 3 items

tests/test_call.py ==============영화목록==============
!!!데이터가 이미 존재합니다!!! : /home/kimpass189/data/movies/year=2015/data.json
================================
.==============영화상세정보==============
!!!데이터가 이미 존재합니다!!! : /home/kimpass189/data/movies/movieinfo/year=2015/data.json
================================
.==============영화사목록==============
  1%|▍                                                                               | 7/1331 [00:42<2:13:20,  6.04s/it]
```
***
# Error!!
## JsonDecoderError - 해결중
```bash
$ pytest -s
E           requests.exceptions.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

.venv/lib/python3.11/site-packages/requests/models.py:978: JSONDecodeError
=============================================== short test summary info ================================================
FAILED tests/test_call.py::test_cplist - requests.exceptions.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
============================================= 1 failed, 2 passed in 43.64s =============================================
```
