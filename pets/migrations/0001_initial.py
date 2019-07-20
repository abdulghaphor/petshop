# Generated by Django 2.2.3 on 2019-07-20 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('age', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='restaurant_logos')),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]
