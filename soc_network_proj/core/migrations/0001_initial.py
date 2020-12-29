# Generated by Django 3.1.4 on 2020-12-25 16:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('hunter_verified', models.CharField(choices=[('NF', 'Not Verified'), ('VL', 'Valid'), ('NV', 'Not Valid')], default='NF', max_length=2)),
                ('clearbit_enriched', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClearBitProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clearbit_id', models.PositiveBigIntegerField(blank=True, null=True)),
                ('clearbit_full_name', models.CharField(blank=True, max_length=300)),
                ('clearbit_given_name', models.CharField(blank=True, max_length=100)),
                ('clearbit_family_name', models.CharField(blank=True, max_length=200)),
                ('clearbit_comp_id', models.PositiveIntegerField(blank=True, null=True)),
                ('clearbit_comp_name', models.CharField(blank=True, max_length=100)),
                ('clearbit_comp_legal_name', models.CharField(blank=True, max_length=200)),
                ('clearbit_comp_domain', models.URLField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='clearbit', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
