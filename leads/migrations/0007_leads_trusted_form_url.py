# Generated by Django 4.2.4 on 2024-03-21 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0006_jornayauser_rename_client_leads_user_leads_cleint_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='leads',
            name='trusted_form_url',
            field=models.URLField(blank=True, null=True, unique=True),
        ),
    ]
