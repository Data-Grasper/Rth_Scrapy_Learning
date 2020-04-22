#引入文件
import scrapy
# 定义容器来保存爬取的数据
class CourseItem(scrapy.Item):
    #课程标题
    title = scrapy.Field()
    #课程url
    url = scrapy.Field()
    #课程标题图片
    image_url = scrapy.Field()
    #课程描述
    introduction = scrapy.Field()
    #学习人数
    student = scrapy.Field()
    #图片地址
    image_path = scrapy.Field()

# 容器操作举例：使用类似于字典的API
course = CourseItem()
# 赋值
course['title']="语文"
# 取值
print(course.get('title'))
# 获取全部键
print(course.keys())
# 获取全部值
print(course.items())