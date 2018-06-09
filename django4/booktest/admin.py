from django.contrib import admin
from booktest import  models

# Register your models here.
#关联添加
class BookInlime(admin.TabularInline):
    model = models.Book
    extra = 2
class BookAdmin(admin.ModelAdmin):
    list_display = ('name','createTime') #显示字段，可以点击列头排序
    list_filter = ['name'] #过滤框，会出现在右侧
    search_fields = ['name'] #搜索框
    list_per_page = 5 # 分页框

class BookTypeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [BookInlime]

#将模型注册到admin中
admin.site.register(models.Book,BookAdmin)
admin.site.register(models.BookType,BookTypeAdmin)