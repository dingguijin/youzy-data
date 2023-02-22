import os
import json
import time
import random
import requests

from api_school import get_schools_ids
from api_province import get_provinces_types
from api_batch import get_batches
from api_url import get_special_plan_url

def _json_write(_school, _province, _local_type, _batch, d):
    _plan_json_path = "api-sp-score/%s_%s_%s_%s.json" % (_school, _province, _local_type, _batch)
    _plan = json.dumps(d, indent=2, ensure_ascii=False)
    with open(_plan_json_path, "w") as _f:
        _f.write(_plan)
    return

def _json_exists(_school, _province, _local_type, _batch):
    _plan_json_path = "api-sp-score/%s_%s_%s_%s.json" % (_school, _province, _local_type, _batch)
    if os.path.exists(_plan_json_path):
        return True
    return False
    
def _main():
    _schools = get_schools_ids()
    _types = get_provinces_types()

    for _school in _schools:
        print("school: %s" % _school)
        for _province in _types:
            #print("province: %s" % _province)
            #print(_types[_province])
            _province_types = _types[_province]
            for _type in _province_types:
                _local_type = _type["id"]
                _batches = get_batches(_province, _school, _local_type)
                if not _batches:
                    continue
                for _batch in _batches:
                    if _json_exists(_school, _province, _local_type, _batch):
                        continue

                    _headers = {
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
                    }

                    _page = 1
                    _size = 10
                    _r_jsons = []
                    _count = 0
                    while True:
                        _url = get_special_score_url(_school,
                                                    _province,
                                                    _local_type,
                                                    _batch,
                                                    2022,
                                                    _size,
                                                    _page)
                        print(_url)
                        time.sleep(float(random.randint(2450, 3800))/1000.0)
                        response = requests.get(_url, headers=_headers)
                        print(response.status_code)
                        print(response.text)
                        if response.status_code != 200:
                            break
                        
                        _r_json = response.json()
                        if int(_r_json.get("code")) != 0:
                            break
                        _r_jsons.append(_r_json)
                        _found = _r_json.get("data").get("numFound")
                        _count += _page * _size
                        if _found <= _count:
                            break
                        else:
                            _page += 1
                            
                            
                    if _r_jsons:
                        _json_write(_school, _province, _local_type, _batch, _r_jsons)
                    
                
    return

if __name__ == "__main__":
    _main()
