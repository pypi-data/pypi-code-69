# Generated by Django 3.1.1 on 2020-09-13 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyCode', models.CharField(max_length=2, verbose_name='firma')),
            ],
            options={
                'verbose_name': 'firma',
                'verbose_name_plural': 'firmaer',
            },
        ),
        migrations.CreateModel(
            name='CostCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=4, verbose_name='verdi')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='beskrivelse')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cost_centers', to='employee_info.company', verbose_name='firma')),
            ],
            options={
                'verbose_name': 'ansvar',
                'verbose_name_plural': 'ansvar',
                'unique_together': {('company', 'value')},
            },
        ),
        migrations.CreateModel(
            name='WorkPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=4, verbose_name='verdi')),
                ('description', models.CharField(max_length=200, verbose_name='beskrivelse')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='work_places', to='employee_info.company', verbose_name='firma')),
            ],
            options={
                'verbose_name': 'arbeidssted',
                'verbose_name_plural': 'arbeidssteder',
                'unique_together': {('company', 'value')},
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resourceId', models.IntegerField(verbose_name='ressursnummer')),
                ('firstName', models.CharField(max_length=200, verbose_name='fornavn')),
                ('lastName', models.CharField(max_length=200, verbose_name='etternavn')),
                ('socialSecurityNumber', models.CharField(max_length=11, verbose_name='fødselsnummer')),
                ('status', models.CharField(max_length=1)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='resource', to='employee_info.company', verbose_name='firma')),
            ],
            options={
                'verbose_name': 'ansatt',
                'verbose_name_plural': 'ansatte',
                'unique_together': {('company', 'resourceId')},
            },
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='navn')),
                ('orgId', models.CharField(max_length=6, verbose_name='nummer')),
                ('status', models.CharField(max_length=1)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='organisation', to='employee_info.company', verbose_name='firma')),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='manages', to='employee_info.resource', verbose_name='leder')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='employee_info.organisation', verbose_name='overordnet')),
            ],
            options={
                'verbose_name': 'organisasjonsenhet',
                'verbose_name_plural': 'organisasjonsenheter',
                'unique_together': {('company', 'orgId')},
            },
        ),
        migrations.CreateModel(
            name='Function',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=4, verbose_name='verdi')),
                ('description', models.CharField(max_length=200, verbose_name='beskrivelse')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='functions', to='employee_info.company', verbose_name='firma')),
            ],
            options={
                'verbose_name': 'funksjon',
                'verbose_name_plural': 'funksjoner',
                'unique_together': {('company', 'value')},
            },
        ),
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employmentType', models.CharField(max_length=1)),
                ('employmentTypeDescription', models.CharField(max_length=200, verbose_name='ansettelsestype')),
                ('mainPosition', models.BooleanField(verbose_name='primært stillingsforhold')),
                ('percentage', models.FloatField(verbose_name='prosent')),
                ('postId', models.IntegerField()),
                ('postIdDescription', models.CharField(max_length=200)),
                ('postCode', models.IntegerField(verbose_name='stillingskode')),
                ('postCodeDescription', models.CharField(max_length=200)),
                ('dateFrom', models.DateField(verbose_name='dato fra')),
                ('dateTo', models.DateField(verbose_name='dato til')),
                ('costCenter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='employments', to='employee_info.costcenter', verbose_name='ansvar')),
                ('function', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='employments', to='employee_info.function', verbose_name='funksjon')),
                ('organisation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='employments', to='employee_info.organisation', verbose_name='organisasjonsenhet')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employments', to='employee_info.resource', verbose_name='ansatt')),
                ('workPlace', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='employments', to='employee_info.workplace', verbose_name='arbeidssted')),
            ],
            options={
                'verbose_name': 'stillingsforhold',
                'verbose_name_plural': 'stillingsforhold',
            },
        ),
    ]
