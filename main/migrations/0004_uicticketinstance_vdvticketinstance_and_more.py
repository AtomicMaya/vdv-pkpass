# Generated by Django 4.2.16 on 2024-10-08 16:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_alter_ticketinstance_options_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="UICTicketInstance",
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
                    models.CharField(max_length=20, verbose_name="Ticket ID"),
                ),
                (
                    "distributor_rics",
                    models.PositiveIntegerField(
                        validators=[django.core.validators.MaxValueValidator(9999)],
                        verbose_name="Distributor RICS",
                    ),
                ),
                ("issuing_time", models.DateTimeField()),
                ("barcode_data", models.BinaryField()),
                ("decoded_data", models.JSONField()),
            ],
            options={
                "ordering": ["-issuing_time"],
            },
        ),
        migrations.AlterField(
            model_name="ticket",
            name="pkpass_authentication_token",
            field=models.CharField(
                default=main.models.make_pass_token,
                max_length=255,
                verbose_name="PKPass authentication token",
            ),
        ),
        migrations.RenameModel(
            old_name="TicketInstance",
            new_name="VDVTicketInstance",
        ),
        migrations.AddField(
            model_name="uicticketinstance",
            name="ticket",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="uic_instances",
                to="main.ticket",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="vdvticketinstance",
            unique_together={("ticket_number", "ticket_org_id")},
        ),
        migrations.AlterUniqueTogether(
            name="uicticketinstance",
            unique_together={("reference", "distributor_rics")},
        ),
    ]
