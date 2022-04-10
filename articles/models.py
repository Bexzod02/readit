from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Tag(models.Model):
    tag = models.CharField(max_length=221)

    def __str__(self):
        return self.tag


class Article(models.Model):
    title = models.CharField(max_length=221)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField()
    image = models.ImageField(upload_to='articles')
    content = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    name = models.CharField(max_length=221)
    image = models.ImageField(upload_to='articles/comment_author', null=True, blank=True)
    email = models.EmailField()
    website = models.URLField(null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


