# Generated by Django 5.0.9 on 2024-11-18 09:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_alter_ticket_ticket_type_rsp6ticketinstance'),
    ]

    operations = [
        migrations.CreateModel(
            name='ELBTicketInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pnr', models.CharField(max_length=6, verbose_name='PNR')),
                ('sequence_number', models.PositiveSmallIntegerField(verbose_name='Sequence number')),
                ('barcode_data', models.BinaryField()),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='elb_instances', to='main.ticket')),
            ],
            options={
                'verbose_name': 'ELB ticket',
                'unique_together': {('pnr', 'sequence_number')},
            },
        ),
    ]