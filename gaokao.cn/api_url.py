from hashlib import md5
from hashlib import sha1
import hmac
import base64

def _hash_hmac(key, code):
    hmac_code = hmac.new(key.encode(), code.encode(), sha1).digest()
    return base64.b64encode(hmac_code).decode()

def _signsafe(url):
    k = 'D23ABC@#56'
    b_64_t = _hash_hmac(k, url)
    m = md5(b_64_t.encode()).hexdigest()
    return m

def get_special_score_url(school_id, province_id,
                          local_type, local_batch,
                          year, size, page):
    t = 'https://api.eol.cn/web/api/?local_batch_id=%s&local_province_id=%s&local_type_id=%s&page=%s&school_id=%s&size=%s&special_group=&uri=apidata/api/gk/score/special&year=%s' % (local_batch, province_id, local_type, page, school_id, size, year)
    return t + "&signsafe=" + _signsafe(t)

def get_special_plan_url(school_id, province_id,
                         local_type, local_batch,
                         year, size, page):
    t = 'https://api.eol.cn/web/api/?local_batch_id=%s&local_province_id=%s&local_type_id=%s&page=%s&school_id=%s&size=%s&special_group=&uri=apidata/api/gkv3/plan/school&year=%s' % (local_batch, province_id, local_type, page, school_id, size, year)
    return t + "&signsafe=" + _signsafe(t)
