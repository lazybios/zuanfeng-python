#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO:
# 1. 定义异常 {u'message': u'param is missing or the value is empty: theme', u'error': u'ParameterInvalid'}
# 2. 检查参数 （装饰器版本）
# 3. 返回失败消息的secrets列表
import requests

class ZuanFeng(object):
    @classmethod
    def push(self, secret, **meta):
        push_url = 'http://zf.omgm4j.com/api/v1/%s/send' % (secret)

        theme = meta.get('theme', 'miss theme')
        title = meta.get('title', 'miss title')
        summary = meta.get('summary', 'miss summary')
        content = meta.get('content', '')

        payload = {'theme': theme, 'title': title, 'summary': summary}

        if content:
          payload['content'] = content

        resp = requests.post(push_url, params = payload)
        ret = resp.json()

        return ret['ok'] == 0


    @classmethod
    def push_batch(self, secrets = [], **meta):
        theme = meta.get('theme', 'miss theme')
        title = meta.get('title', 'miss title')
        summary = meta.get('summary', 'miss summary')
        content = meta.get('content', '')

        errors = []
        for secret in secrets:
          push_url = 'http://zf.omgm4j.com/api/v1/%s/send' % (secret)

          payload = {
            'theme': theme,
            'title': title,
            'summary': summary
          }

          if content:
            payload['content'] = content

          resp = requests.post(push_url, params = payload)
          ret = resp.json()

          errors.append(ret['ok'] == 0)

        results = set(errors)
        if len(results) > 1:
          return False
        else:
          return results.pop() == True

        

if __name__ == '__main__':
    # print ZuanFeng.push('your secret key')
