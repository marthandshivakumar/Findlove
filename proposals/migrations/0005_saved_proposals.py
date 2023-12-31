# Generated by Django 4.2.5 on 2023-10-21 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0004_proposal_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='saved_proposals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(default=0)),
                ('title', models.CharField(max_length=200)),
                ('company_name', models.CharField(max_length=200)),
                ('contact_name', models.CharField(max_length=100)),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_phone', models.CharField(max_length=15)),
                ('proposal_summary', models.TextField()),
                ('project_planning', models.TextField()),
                ('financing', models.TextField()),
            ],
        ),
    ]
