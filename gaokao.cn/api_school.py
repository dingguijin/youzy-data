import json

def get_schools_ids():
    f = open("name.json")
    x = f.read()
    f.close()
    x = eval(x)
    # print(json.dumps(x, indent=2, ensure_ascii=False))
    z = list(map(lambda y: y["school_id"], x["data"]))
    return z
