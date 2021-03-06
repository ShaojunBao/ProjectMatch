# Generated by Django 3.2.8 on 2022-03-31 03:30

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppUserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector', models.CharField(blank=True, max_length=30)),
                ('interests', models.TextField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AppUser',
            fields=[
            ],
            options={
                'ordering': ('username',),
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField(max_length=500)),
                ('attachments', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='landing.appuserprofile')),
            ],
        ),
        migrations.AddField(
            model_name='appuserprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='landing.appuser'),
        ),
    ]
