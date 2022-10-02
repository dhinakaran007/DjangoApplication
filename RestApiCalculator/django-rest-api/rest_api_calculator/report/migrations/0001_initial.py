# Generated by Django 2.2.5 on 2019-09-21 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='APIRequestLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_name', models.CharField(db_index=True, max_length=200, verbose_name='API Name')),
                ('requested_at', models.DateTimeField(db_index=True)),
                ('latency', models.PositiveIntegerField(default=0)),
                ('errors', models.TextField(blank=True, null=True)),
                ('status_code', models.PositiveIntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]