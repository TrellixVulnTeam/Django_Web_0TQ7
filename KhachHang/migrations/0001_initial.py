# Generated by Django 2.2 on 2021-01-13 06:47

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('address', models.CharField(default='', max_length=255)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(0, 'Khiếu nại'), (1, 'Báo cáo'), (2, 'Đánh giá')], default=0)),
                ('title', models.CharField(default='', max_length=255)),
                ('content', models.CharField(default='', max_length=255)),
                ('create_day', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.IntegerField(choices=[(0, 'Đã xem'), (1, 'Chưa xem'), (2, 'Đã phản hồi')], default=1)),
                ('reporter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, null=True)),
                ('phone', models.CharField(max_length=11, null=True)),
                ('address', models.CharField(default='', max_length=255, null=True)),
                ('avatar', models.ImageField(upload_to='')),
                ('sex', models.IntegerField(choices=[(0, 'Nữ'), (1, 'Nam')], default=0, null=True)),
                ('create_day', models.DateTimeField(auto_now_add=True, null=True)),
                ('date', models.DateTimeField(null=True)),
                ('status', models.BooleanField(default=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('price', models.FloatField(default=0.0)),
                ('quantity', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('image', models.ImageField(upload_to='')),
                ('description', models.CharField(default='', max_length=500)),
                ('status', models.BooleanField(default=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='KhachHang.category')),
                ('label', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='KhachHang.label')),
                ('supplier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='KhachHang.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('ordered', models.BooleanField(default=False)),
                ('trade_time', models.IntegerField(default=0, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KhachHang.product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('ordered', models.BooleanField(default=False)),
                ('trade_time', models.IntegerField(default=0, null=True)),
                ('items', models.ManyToManyField(to='KhachHang.OrderItem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('content', models.CharField(default='', max_length=255)),
                ('create_day', models.DateTimeField(null=True)),
                ('status', models.BooleanField(default=True)),
                ('img', models.ImageField(null=True, upload_to='')),
                ('sumary', models.TextField(default='', max_length=255)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='label',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KhachHang.label'),
        ),
        migrations.CreateModel(
            name='bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('totalprice', models.FloatField(default=0)),
                ('trade_time', models.IntegerField(default=0, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('Order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='KhachHang.Order')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]