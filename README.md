# zuanfeng-python
zuanfeng sdk for python

### TODO
+ 异常处理(`ParameterInvalid、SecretInvalid`)
+ 检查参数 （装饰器版本）
+ 返回失败消息的secrets列表


### Install
```
pip install zuanfeng
```

### Usage
```
import zuanfeng

# content is optional
zuanfeng.push('your secret key', theme = '', title = '', summary = '', content = '')

# your secret list
secrets = [...]

# content is optional
zuanfeng.push_batch(secrets, theme = '', title = '', summary = '', content = '')
```