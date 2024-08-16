from mvstar.app import mkjson

def test_json():
    for i in range(2015 ,2022):
        r = mkjson(dt=i, sleep_time=0.1)
        assert r
