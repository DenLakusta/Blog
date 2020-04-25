from django.db import models
from datetime import datetime
# Create your models here.
from django.urls import reverse







class Category(models.Model):
    title = models.CharField("Category", max_length=150)
    slug = models.SlugField("Slug", max_length=50, unique=True)
    description = models.TextField('Description', max_length=2000, default='')


    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Tag(models.Model):
    title = models.CharField("Tag", max_length=150)
    slug = models.SlugField("Slug", max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse("tag_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

class Author(models.Model):
    name = models.CharField("Name", max_length=50)
    email = models.EmailField("Email", max_length=150, null=True)
    slug = models.SlugField("Slug", max_length=150, unique=True)
    image = models.ImageField("Post image", upload_to="authors_image/", null=True)
    about = models.TextField('About me', max_length=5000, null=True)
    date_birth = models.CharField('Date of birth', max_length=10, blank=True)

    # posts = models.ManyToManyField(Post, verbose_name="Posts", related_name='hanabis_blog', blank=True)

    def get_absolute_url(self):
        return reverse("author_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name

    class Meta:

        verbose_name = "Author"
        verbose_name_plural = "Authors"


class Post(models.Model):
    title = models.CharField("Title", max_length=150, db_index=True)
    slug = models.SlugField("Slug", max_length=150, unique=True)
    body = models.TextField("Body", db_index=True)
    tags = models.ManyToManyField(Tag, verbose_name="tags", related_name="posts", blank=True)
    date_pub = models.DateTimeField("Date", default="")
    auth = models.ManyToManyField(Author, verbose_name="Authors", related_name='posts', blank=True)
    image = models.ImageField("Post image", upload_to="post_image/")
    draft = models.BooleanField("Draft", default=False)
    category = models.ForeignKey(Category, verbose_name="Categories", on_delete=models.SET_NULL, null=True, related_name='posts')

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug":self.slug})
    
    def __str__(self):
        return self.title

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    class Meta:
        ordering = ['-date_pub']
        verbose_name = "Post"
        verbose_name_plural = "Posts"



class Reviews(models.Model):

    name = models.CharField('Name', max_length=100, null=True, blank=True)
    email = models.EmailField("Email", max_length=150, null=True, blank=True)
    text = models.TextField('Message', max_length=5000)
    parent = models.ForeignKey('self', verbose_name='Parent', on_delete=models.SET_NULL, blank=True, null=True)
    date_pub = models.CharField("Date",null=True, blank=True, auto_created=True, default=datetime.now().strftime('%Y-%m-%d'), max_length=50)
    post = models.ForeignKey(Post, verbose_name='post', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.post}"

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
