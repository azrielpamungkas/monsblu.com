from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

STATUS  = (
    (0, 'Draft'),
    (1, 'Publish')
)

class Post(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=50, null=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    content = RichTextUploadingField()
    tag = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.DateField(null=True, blank=True, editable=False)
    status = models.BooleanField(choices=STATUS, default=0)

    def get_absolute_url(self):
        return reverse('tutorial_detail', args=[self.slug])

    def save(self,*args):
        if not self.slug:
            self.slug = slugify(self.title)
        if self.status is True:
            self.published = timezone.now()
        return super().save(*args)

    def __str__(self):
        return self.title