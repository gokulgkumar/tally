# Generated by Django 4.2.3 on 2023-11-06 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0029_remove_companies_distributors_delete_distributor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_details', models.CharField(blank=True, max_length=100, null=True)),
                ('start_date', models.DateField(blank=True, max_length=255, null=True)),
                ('end_date', models.DateField(blank=True, max_length=255, null=True)),
                ('distributor_id', models.CharField(blank=True, max_length=100, null=True)),
                ('logins', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.logins')),
                ('payment_terms', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.payment_terms')),
            ],
        ),
    ]
