import json
import requests
import time
import random
import path

def _get_schools():
    f = open("name.json")
    x = f.read()
    f.close()
    x = eval(x)
    # print(json.dumps(x, indent=2, ensure_ascii=False))
    z = list(map(lambda y: y["school_id"], x["data"]))
    return z

def _get_provinces():
    f = open("province_control.json")
    x = f.read()
    f.close()
    x = eval(x)
    ps = x["data"]["province"]
    return ps

def _get_provinces_types():
    f = open("province_control.json")
    x = f.read()
    f.close()
    x = eval(x)

    ps = x["data"]["province"]
    types = x["data"]["type"]

    keys = list(map(lambda p: "%s_2022" % p, ps))
    ktypes = list(map(lambda k: types[k], keys))
    return ktypes

def _get_province_school_score(year, province_id, school_id, type_id):
    _url = "https://static-data.gaokao.cn/www/2.0/schoolprovinceindex/%s/%s/%s/%s/1.json" % (year, school_id, province_id, type_id)

    _path = "api_json/%s_%s_%s_%s_1.json" % (year, school_id, province_id, type_id)
    if path.exists(_path):
        return None
        
    print(_url)
    response = requests.get(_url)
    print(response.status_code)
    if response.status_code != 200:
        return
    else:
        with open(_path, "w") as f:
            _r = response.json()
            f.write(json.dumps(_r, indent=2, ensure_ascii=False))
    return
    
def _main():
    _schools = _get_schools()
    print("total schools %d" % len(_schools))
    _provinces = _get_provinces()
    _types = _get_provinces_types()

    _scores_array = []
    for _index, _p in enumerate(_provinces):
        _t = _types[_index]
        _ts = list(map(lambda x: x["id"], _t))
        for _s in _schools:
            for _i_ts in _ts:
                #time.sleep(float(random.randint(100, 200))/1000.0)
                _get_province_school_score(2022, _p, _s, _i_ts)
            
    return

if __name__ == "__main__":
    _main()
