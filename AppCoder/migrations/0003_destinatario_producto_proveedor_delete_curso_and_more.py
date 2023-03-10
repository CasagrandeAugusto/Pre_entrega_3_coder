# Generated by Django 4.1.6 on 2023-03-10 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destinatario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreD', models.CharField(max_length=40)),
                ('apellidoD', models.CharField(max_length=40)),
                ('telefonoD', models.IntegerField()),
                ('direccionD', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreProducto', models.CharField(max_length=40)),
                ('categoria', models.CharField(max_length=40)),
                ('fechaingreso', models.DateField()),
                ('costo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreP', models.CharField(max_length=40)),
                ('apellidoP', models.CharField(max_length=40)),
                ('telefonoP', models.IntegerField()),
                ('direccionP', models.CharField(max_length=40)),
            ],
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
        migrations.DeleteModel(
            name='Entregable',
        ),
        migrations.DeleteModel(
            name='Estudiante',
        ),
        migrations.DeleteModel(
            name='Profesor',
        ),
        migrations.AlterField(
            model_name='avatar',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
    ]
