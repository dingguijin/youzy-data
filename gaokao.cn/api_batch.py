import json
import os

def get_batches(province_id, school_id, local_type, year=2022):
    _score_path = "api-json/score/api-json/%s_%s_%s_%s_1.json" % (year, school_id,
                                                                  province_id, local_type)
    
    if not os.path.exists(_score_path):
        return None
    
    f = open(_score_path)
    x = f.read()
    f.close()
    x = eval(x)

    if not x:
        return None

    _items = x["data"]["item"]
    _batches = list(map(lambda i: i["batch"], _items))
    return _batches
