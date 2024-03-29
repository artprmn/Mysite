# Generated by Django 4.2.1 on 2024-02-05 03:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0002_house_campaign'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='houses',
        ),
        migrations.AddField(
            model_name='house',
            name='campaign',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.campaign'),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='house',
            name='apartments_per_entrance',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='house',
            name='city',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='house',
            name='entrances',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='house',
            name='street',
            field=models.CharField(max_length=255),
        ),
    ]
