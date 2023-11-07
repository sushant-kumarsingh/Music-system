# Generated by Django 4.2.3 on 2023-10-31 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('albumName', models.CharField(max_length=50, verbose_name='Album Name')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Artist created date')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Latest artist update')),
            ],
            options={
                'verbose_name': 'Album',
                'verbose_name_plural': 'Albums',
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artistName', models.CharField(max_length=50, verbose_name='Artist Name')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Artist created date')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Latest artist update')),
            ],
            options={
                'verbose_name': 'Artist',
                'verbose_name_plural': 'Artists',
            },
        ),
        migrations.CreateModel(
            name='song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('songThumbnail', models.ImageField(help_text='.jpg ,.png, .gif ,.svg supported', upload_to='thumbnail/', verbose_name='song Thumbnail')),
                ('song', models.FileField(help_text='.mp3 supported only', upload_to='songs/', verbose_name='song')),
                ('songName', models.CharField(max_length=50, verbose_name='song Name')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='song created date')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Latest song update')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1_music.album', verbose_name='song Album')),
            ],
            options={
                'verbose_name': 'song',
                'verbose_name_plural': 'songs',
            },
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1_music.artist', verbose_name='Artist Album'),
        ),
    ]
