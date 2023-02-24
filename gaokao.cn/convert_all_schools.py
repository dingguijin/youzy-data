import os



def _main():
    _dir = "proxy_filter/all_schools/2023-2-15/api.eol.cn/web/api"
    _js = []
    for _x in os.walk(_dir):
        _jsons = list(_x)[2]
        for _j in _jsons:
            _y = _dir + "/" + _j
            with open(_y) as _f:
                _js += eval(_f.read())["data"]["item"]

    print(len(_js))
    print(_js)

    return

if __name__ == "__main__":
    _main()
