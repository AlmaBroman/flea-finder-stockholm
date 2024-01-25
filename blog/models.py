from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from cloudinary.models import CloudinaryField
from django_resized import ResizedImageField


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField()
    start_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    adress = models.CharField('adress', max_length=1024)
    map_link = models.URLField(max_length=200)
    featured_image = ResizedImageField(size=[1000, None], quality=75, upload_to='blog/', force_format='WEBP', default='placeholder')
    image_alt = models.CharField(max_length=100, default='event image')
    created_on = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=200, default='uncategorized')
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    # approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return self.title
    
    def number_of_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']
    
    def __str__(self):
        return f"Comment {self.body} by {self.name}"
