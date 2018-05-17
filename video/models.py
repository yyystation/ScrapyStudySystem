import datetime
from django.db import models


# Create your models here.

class User(models.Model):
    id = models.AutoField(max_length=30, primary_key=True)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=10)
    phone = models.CharField(max_length=12, blank=False, null=False)
    email = models.CharField(max_length=75, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True, default=datetime.datetime.now)
    last_login_time = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.username

    def __unicode__(self):
        return self.username


class Media(models.Model):
    media_id = models.AutoField(max_length=30, primary_key=True)
    url = models.CharField(max_length=255)
    pic_url = models.CharField(max_length=255)
    title = models.CharField(max_length=100)
    intro = models.CharField(max_length=200, blank=True)
    tag = models.CharField(max_length=50,null=True)
    like_num = models.IntegerField(blank=True)
    comment_num = models.IntegerField(blank=True)
    view_num = models.IntegerField(blank=True)
    source = models.CharField(max_length=20)
    duration = models.CharField(max_length=20, blank=True)
    update_time = models.DateTimeField(blank=True, default=datetime.datetime.now)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    comment_id = models.AutoField(max_length=30, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    pub_time = models.DateTimeField(blank=False, null=False, default=datetime.datetime.now)
    up_num = models.IntegerField()
    down_num = models.IntegerField()

    def __str__(self):
        return self.comment_id

    def __unicode__(self):
        return self.comment_id


class Like(models.Model):
    like_id = models.AutoField(max_length=30, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    pub_time = models.DateTimeField(blank=False, null=False, default=datetime.datetime.now)

    def __str__(self):
        return self.like_id

    def __unicode__(self):
        return self.like_id


class history(models.Model):
    history_id = models.AutoField(max_length=30, primary_key=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    view_time = models.DateTimeField(blank=False, null=False, default=datetime.datetime.now)

    def __str__(self):
        return self.history_id

    def __unicode__(self):
        return self.history_id
