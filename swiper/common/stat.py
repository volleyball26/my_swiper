'''前后端的状态码'''

OK = 0  # 正常
SEND_FAILD = 1000  # 验证码发送失败
VOCDE_ERR = 1001  # 验证码错误


LOGIN_REQUIRED = 1002  # 需要用户登陆
PROFILE_ERR = 1003  # 用户资料表单数据错误
SID_ERR = 1004  # SID 错误
STYPE_ERR = 1005  # 滑动类型错误
SWIPE_REPEAT = 1006  # 重复滑动
REWIND_LIMITED = 1007  # 反悔次数达到限制
REWIND_TIMEOUT = 1008  # 反悔超时
NO_SWIPE = 1009  # 当前还没有滑动记录
PERM_ERR = 1010  # 用户不具有某权限
