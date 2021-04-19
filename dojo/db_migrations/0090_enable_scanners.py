# Generated by Django 2.2.20 on 2021-04-19 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0089_unprotect_jira_project'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tool_type',
            options={'ordering': ['name', 'description', 'enabled']},
        ),
        migrations.AddField(
            model_name='tool_type',
            name='enabled',
            field=models.BooleanField(default=True, help_text='Enables or disables scanner'),
        ),
    ]
