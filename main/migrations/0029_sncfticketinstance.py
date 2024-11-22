# Generated by Django 5.0.9 on 2024-11-17 20:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0028_alter_ticket_photos"),
    ]

    operations = [
        migrations.CreateModel(
            name="SNCFTicketInstance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "reference",
                    models.CharField(
                        max_length=20, unique=True, verbose_name="Ticket number"
                    ),
                ),
                ("barcode_data", models.BinaryField()),
                (
                    "ticket",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sncf_instances",
                        to="main.ticket",
                    ),
                ),
            ],
            options={
                "verbose_name": "SNCF ticket",
            },
        ),
    ]