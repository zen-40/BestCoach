# Generated by Django 3.2.17 on 2023-03-01 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overview_app', '0002_auto_20230301_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simplecms',
            name='section_team_6_description',
            field=models.TextField(default='<li class="mb-2">Amet minim mollit deserunt ullamco</li>\n<li class="mb-2">Velit officia consequat duis enim</li>\n<li>Exercitation veniam minim</li>'),
        ),
        migrations.AlterField(
            model_name='simplecms',
            name='section_up_footer_9_title',
            field=models.TextField(default='Ready to <br class="d-none d-xxl-inline">Get Started?'),
        ),
    ]