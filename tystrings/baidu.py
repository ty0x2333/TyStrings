import requests
import random
import hashlib
import json


class BaiduTranslator(object):
    def __init__(self, app_id, secret_key, https_enable=False):
        self.app_id = app_id
        self.secret_key = secret_key
        self.api_host = 'https://fanyi-api.baidu.com' if https_enable else 'http://api.fanyi.baidu.com'

    def translate(self, question, dst_lang, src_lang='auto'):
        result = {}
        if not question:
            return result
        salt = random.randint(32768, 65536)
        md5 = hashlib.md5()
        md5.update(self.app_id + question + str(salt) + self.secret_key)
        sign = md5.hexdigest()
        params = {'appid': self.app_id,
                  'q': question,
                  'from': 'auto' if src_lang is None else src_lang,
                  'to': dst_lang,
                  'salt': salt,
                  'sign': sign}
        response = requests.get(self.api_host + '/api/trans/vip/translate', params=params)
        response_obj = json.loads(response.text)
        trans_results = response_obj['trans_result']
        for trans in trans_results:
            result[trans['src']] = trans['dst']
        return result

    def translate_list(self, questions, dst_lang, src_lang='auto'):
        return self.translate('\n'.join(questions), dst_lang, src_lang)