from mvstar.app import mkjson

def test_json():
    r = mkjson(dt=2015, sleep_time=0.1)
    assert r

