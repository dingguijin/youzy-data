import json

def get_provinces_ids():
    f = open("province_control.json")
    x = f.read()
    f.close()
    x = eval(x)
    ps = x["data"]["province"]
    return ps

def get_provinces_types(year="2022"):
    f = open("province_control.json")
    x = f.read()
    f.close()
    x = eval(x)

    ps = x["data"]["province"]
    types = x["data"]["type"]

    keys = list(map(lambda p: "%s_%s" % (p, year), ps))
    ktypes = list(map(lambda k: types[k], keys))
    
    return dict(zip(ps, ktypes))
