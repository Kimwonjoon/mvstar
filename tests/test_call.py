from mvstar.app import mkjson
from mvstar.mvinfo import read_data

def test_json():
    for i in range(2015 ,2022):
        r = mkjson(dt=i, sleep_time=0.1)
        assert r
def test_info():
    for i in range(2015 ,2022):
        r = read_data(dt = i, sleep_time = 0.1)
        assert r
