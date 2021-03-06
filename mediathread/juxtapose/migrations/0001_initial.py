# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('djangosherd', '0003_auto_20150721_1435'),
        ('courseaffils', '0003_auto_20160429_1353'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JuxtaposeAsset',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.TextField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('course', models.ForeignKey(to='courseaffils.Course')),
                ('spine', models.ForeignKey(
                    blank=True, to='djangosherd.SherdNote', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='JuxtaposeMediaElement',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('start_time', models.DecimalField(
                    max_digits=8, decimal_places=5)),
                ('end_time', models.DecimalField(
                    max_digits=8, decimal_places=5)),
                ('juxtaposition', models.ForeignKey(
                    to='juxtapose.JuxtaposeAsset')),
                ('media', models.ForeignKey(to='djangosherd.SherdNote')),
            ],
        ),
        migrations.CreateModel(
            name='JuxtaposeTextElement',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('start_time', models.DecimalField(
                    max_digits=8, decimal_places=5)),
                ('end_time', models.DecimalField(
                    max_digits=8, decimal_places=5)),
                ('text', models.TextField()),
                ('juxtaposition', models.ForeignKey(
                    to='juxtapose.JuxtaposeAsset')),
            ],
        ),
    ]
