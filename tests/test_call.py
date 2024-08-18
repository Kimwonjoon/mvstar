from mvstar.app import mkjson
from mvstar.mvinfo import read_data

def test_json():
    print("==============영화목록==============")
    for i in range(2015 ,2022):
        r = mkjson(dt=i, sleep_time=0.1)
        assert r
    print("================================")
def test_info():
    print("==============영화상제정보==============")
    for i in range(2015 ,2022):
        r = read_data(dt = i, sleep_time = 0.1)
        assert r
    print("================================")
