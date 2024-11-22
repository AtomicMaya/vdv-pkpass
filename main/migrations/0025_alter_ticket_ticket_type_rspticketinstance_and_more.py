# Generated by Django 5.0.9 on 2024-11-17 13:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0024_alter_rsp6ticketinstance_unique_together"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ticket",
            name="ticket_type",
            field=models.CharField(
                choices=[
                    ("deutschlandticket", "Deutschlandticket"),
                    ("klimaticket", "Klimaticket"),
                    ("bahncard", "Bahncard"),
                    ("fahrkarte", "Fahrkarte"),
                    ("reservierung", "Reservierung"),
                    ("interrail", "Interrail"),
                    ("railcard", "Railcard"),
                    ("unknown", "Unknown"),
                ],
                default="unknown",
                max_length=255,
                verbose_name="Ticket type",
            ),
        ),
        migrations.CreateModel(
            name="RSPTicketInstance",
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
                ("issuer_id", models.CharField(max_length=2, verbose_name="Issuer ID")),
                (
                    "reference",
                    models.CharField(max_length=20, verbose_name="Ticket reference"),
                ),
                ("barcode_data", models.BinaryField()),
                (
                    "ticket_type",
                    models.CharField(
                        default="06", max_length=2, verbose_name="Ticket type"
                    ),
                ),
                ("decoded_data", models.JSONField()),
                ("validity_start", models.DateTimeField(blank=True, null=True)),
                ("validity_end", models.DateTimeField(blank=True, null=True)),
                (
                    "ticket",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="rsp6_instances",
                        to="main.ticket",
                    ),
                ),
            ],
            options={
                "verbose_name": "RSP ticket",
                "unique_together": {("ticket_type", "reference", "issuer_id")},
            },
        ),
        migrations.DeleteModel(
            name="RSP6TicketInstance",
        ),
    ]