# Generated by Django 4.2.5 on 2023-10-21 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0007_alter_proposal_user_alter_saved_proposals_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proposal',
            old_name='user',
            new_name='username',
        ),
    ]
