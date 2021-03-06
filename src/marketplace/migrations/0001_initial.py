# Generated by Django 3.1.4 on 2021-08-26 03:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('regions', '0001_initial'),
        ('inventory', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Marketplace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Name')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Marketplace',
                'verbose_name_plural': 'Marketplaces',
            },
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('marketplace', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='listing', to='marketplace.marketplace', verbose_name='Marketplace')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='listings', to='regions.region')),
            ],
            options={
                'verbose_name': 'Listing',
                'verbose_name_plural': 'Listings',
                'unique_together': {('name', 'marketplace')},
            },
        ),
        migrations.CreateModel(
            name='MarketplaceItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('status', models.CharField(choices=[('pending_confirmation', 'Pending confirmation'), ('confirmed', 'Confirmed'), ('declined', 'Declined')], db_index=True, default='pending_confirmation', max_length=30)),
                ('status_comment', models.CharField(blank=True, max_length=255, null=True)),
                ('external_id', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='External ID')),
                ('listings', models.ManyToManyField(related_name='marketplace_items', to='marketplace.Listing')),
                ('marketplace', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='marketplace_items', to='marketplace.marketplace')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='marketplace_items', to='inventory.product')),
            ],
            options={
                'verbose_name': 'Marketplace item',
                'verbose_name_plural': 'Marketplace items',
                'unique_together': {('marketplace', 'product'), ('marketplace', 'external_id')},
            },
        ),
    ]
