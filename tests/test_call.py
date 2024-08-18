from mvstar.app import mkjson
from mvstar.mvinfo import read_data
from mvstar.cplist import cpjson
import requests

def test_json():
    print("==============영화목록==============")
#    for i in range(2015 ,2016):
#        r = mkjson(dt=i, sleep_time=0.1)
#        assert r
    r = mkjson(dt = 2015, sleep_time = 0.1)
    assert r
    print("================================")

def test_info():
    print("==============영화상세정보==============")
#    for i in range(2015 ,2016):
#        r = read_data(dt = i, sleep_time = 0.1)
#        assert r
    r = read_data(dt = 2015, sleep_time = 0.1)
    assert r
    print("================================")

def test_cplist():
    print("==============영화사목록==============")
    r = cpjson(pg = 1, sleep_time = 0.5)
    assert r
    print("================================")

