import json
import requests

provinces = ["北京", "天津", "河北", "山西", "内蒙古",
             "辽宁", "吉林", "黑龙江",
             "上海", "江苏", "浙江",
             "安徽", "福建", "江西", "山东", "河南", "湖北", "湖南",
             "广东", "广西", "海南", "重庆", "四川", "贵州", "云南",
             "西藏", "陕西", "甘肃", "青海",  "宁夏", "新疆"]

def get_province_control_url(province_id):
    url = "https://static-data.gaokao.cn/www/2.0/proprovince/%d/pro.json"    
    return url % province_id

def load_province_control_json():
    f = open("province_control.json")
    x = f.read()
    f.close()
    x = eval(x)
    y = []
    #print(json.dumps(x, indent=2, ensure_ascii=False))
    x_province = x["data"]["province"]
    for index, id in enumerate(x_province):
        d = {}
        d["province_name"] = provinces[index]
        d["province_id"] = id        
        y.append(d)
        print(d)

    return y

if __name__ == "__main__":
    load_province_control_json()
