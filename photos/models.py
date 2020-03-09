from django.db import models
from user.models import User
from group.models import Group

# Create your models here.
class Photo(models.Model):

    title = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    group = models.ForeignKey('group.Group', on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    date_posted = models.DateTimeField(null=True, blank=True)
    date_taken = models.DateTimeField(null=True, blank=True)
    date_updated = models.DateTimeField(null=True, blank=True)
    url_page = models.URLField(max_length=255, null=True, blank=True)
    ispublic = models.NullBooleanField()


    # class Meta:
    #     ordering = ('-date_posted', '-date_taken',)
    #     get_latest_by = 'date_posted'

    # def __unicode__(self):
    #     return u'%s' % self.title

    # def get_absolute_url(self):
    #     return reverse('flickr_photo', args=[self.flickr_id, ])

    # @property
    # def flickr_page_url(self):
    #     return '%s%s/' % (self.user.flickr_page_url, self.flickr_id)