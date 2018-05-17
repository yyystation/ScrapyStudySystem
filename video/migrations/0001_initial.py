# Generated by Django 2.0.5 on 2018-05-17 13:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(max_length=30, primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=500)),
                ('pub_time', models.DateTimeField(default=datetime.datetime.now)),
                ('up_num', models.IntegerField()),
                ('down_num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='history',
            fields=[
                ('history_id', models.AutoField(max_length=30, primary_key=True, serialize=False, unique=True)),
                ('view_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('like_id', models.AutoField(max_length=30, primary_key=True, serialize=False)),
                ('pub_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('media_id', models.AutoField(max_length=30, primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=255)),
                ('pic_url', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=100)),
                ('intro', models.CharField(blank=True, max_length=200)),
                ('tag', models.CharField(max_length=50, null=True)),
                ('like_num', models.IntegerField(blank=True)),
                ('comment_num', models.IntegerField(blank=True)),
                ('view_num', models.IntegerField(blank=True)),
                ('source', models.CharField(max_length=20)),
                ('duration', models.CharField(blank=True, max_length=20)),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(max_length=30, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.CharField(blank=True, max_length=75, null=True)),
                ('create_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('last_login_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.AddField(
            model_name='like',
            name='media',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.Media'),
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.User'),
        ),
        migrations.AddField(
            model_name='history',
            name='media',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.Media'),
        ),
        migrations.AddField(
            model_name='history',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.User'),
        ),
        migrations.AddField(
            model_name='comment',
            name='media',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.Media'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.User'),
        ),
    ]
