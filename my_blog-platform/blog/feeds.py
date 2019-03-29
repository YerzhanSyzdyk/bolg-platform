from django.contrib.syndication.views import Feed 

from .models import Post 

class AllPostsRssFeed(Feed):
    title = "寻常的日与夜"

    link = "/"

    description = "可白昼过尽 夜晚来临"

    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return '[%s] %s' % (item.category, item.title)

    def item_description(self, item):
        return item.body
