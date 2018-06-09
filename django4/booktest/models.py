from django.db import models

# Create your models here.
# 自定义管理器
class BookInfoManager1(models.Manager):
    def get_queryset(self):
        print(123)
        return super().get_queryset().filter(isDelete=False)

#书的类型
class BookType(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title
#创建模型
class Book(models.Model):
    #书名
    name = models.CharField(max_length=200)
    createTime = models.DateTimeField()
    remark = models.TextField()
    hTtile = models.ForeignKey(BookType(),on_delete=models.CASCADE)
    readCount = models.IntegerField(default=0 )
    # books = BookInfoManager1()
    isDelete = models.BooleanField(default=False)
    # 元选项
    class Meta:
        db_table = 'bookInfo' # 表名 不指定默认为booktest_bookInfo
        ordering = ['createTime'] # 默认排序功能 字符串前加-表示倒序  会占用磁盘的开销
    # 创建模型类对象的方法(1 使用类方法创建)
    @classmethod
    def createObject(cls,name,createTime):
        b = Book()
        b.name = name
        b.createTime  = createTime
        return b


    def __str__(self):
        return self.name

