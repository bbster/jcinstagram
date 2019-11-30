from django.db import models
from users import models as user_models
from images import models as image_models
#  알람
#  팔로우 알람
#  이미지에 댓글, 좋아요 알람


class Notification(image_models.TimeStampedModel):

    TYPE_CHOICES = {
        ('like', 'Like'),
        ('comment', 'Comment'),
        ('follow', 'Follow'),
    }

    creator = models.ForeignKey(user_models.User, related_name='creator', on_delete=models.CASCADE)
    to = models.ForeignKey(user_models.User, related_name='to', on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    image = models.ForeignKey(image_models.Image, on_delete=models.CASCADE, null=True, blank=True)
    # 장고 2.0부터 on_delete 명시적으로 써줘야함
    comment = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return 'From: {} - To {}'.format(self.creator, self.to)
