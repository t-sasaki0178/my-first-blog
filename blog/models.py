from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User','on_delete')
    title = models.CharField(max_length=200) #テキスト数を定義するフィールド
    text = models.TextField() #制限なしの長いテキスト用。ブログの投稿用？
    created_date = models.DateTimeField(default=timezone.now) #日付と時間のフィールド
    publish_date = models.DateTimeField(blank=True,null=True) #他モデルへのリンク

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title