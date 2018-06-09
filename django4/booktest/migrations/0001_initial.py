# Generated by Django 2.0.5 on 2018-06-01 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('createTime', models.DateTimeField()),
                ('remark', models.TextField()),
                ('readCount', models.IntegerField(default=0)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'bookInfo',
                'ordering': ['createTime'],
            },
        ),
        migrations.CreateModel(
            name='BookType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='hTtile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booktest.BookType'),
        ),
    ]