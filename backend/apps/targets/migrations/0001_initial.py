# Generated by Django 4.0.4 on 2022-05-03 03:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('started', 'Started'), ('working', 'Working'), ('delayed', 'Delayed'), ('failed', 'Failed'), ('achieved', 'Achieved'), ('deleted', 'Deleted')], default='started', max_length=1000, verbose_name='Status')),
                ('type', models.CharField(choices=[('enrollment', 'Enrollment Target'), ('attendance', 'Attendance Target'), ('progress', 'Progress Target'), ('graduation', 'Graduation Target'), ('self_dev_project', 'Self Dev Project Target'), ('group_dev_project', 'Group Dev Project Target'), ('referral', 'Referral Program Target'), ('offer', 'Offer Target')], db_index=True, default='progress', max_length=20, verbose_name='Type of Target')),
                ('target_number', models.CharField(default='100', max_length=3, verbose_name='Target in Percentage')),
                ('cohort', models.CharField(db_index=True, max_length=10, verbose_name='Cohort')),
                ('project_start_date', models.DateTimeField(verbose_name='Project Starting Date')),
                ('project_due_date', models.DateTimeField(max_length=20, verbose_name='Project Due Date')),
                ('project_name', models.CharField(max_length=50, verbose_name='Project Name')),
                ('project_github_link', models.CharField(max_length=200, verbose_name='Project GitHub Link')),
                ('project_student_name', models.CharField(max_length=200, verbose_name='Projects Students Name')),
                ('note', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Note')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'target',
            },
        ),
    ]
