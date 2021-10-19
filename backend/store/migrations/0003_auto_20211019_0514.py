# Generated by Django 3.2.7 on 2021-10-19 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20211019_0453'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-date_created',)},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='prod_desc',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='prod_title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='cat_id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='qty',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='store.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]