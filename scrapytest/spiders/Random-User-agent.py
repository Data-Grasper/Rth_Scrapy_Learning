from fake_useragent import UserAgent
ua = UserAgent()
# 随机选取一个User-agent
print(ua.ie)
# 调用函数给我们返回一个正在维护中的User-agent
print(ua.random)