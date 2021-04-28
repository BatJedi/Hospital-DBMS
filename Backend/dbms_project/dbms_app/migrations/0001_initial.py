# Generated by Django 3.2 on 2021-04-27 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('bill_number', models.IntegerField(primary_key=True, serialize=False)),
                ('bill_type', models.IntegerField(blank=True, null=True)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('subtotal', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('taxes', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('paid', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Bill',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('diagnosis_id', models.IntegerField(primary_key=True, serialize=False)),
                ('results', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'db_table': 'Diagnosis',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('doctor_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('contact_no', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('specialization', models.CharField(blank=True, max_length=30, null=True)),
                ('role', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'Doctor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('contact_no', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('occupation', models.CharField(blank=True, max_length=30, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'Employee',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('medicine_id', models.AutoField(primary_key=True, serialize=False)),
                ('inventory_quantity', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'Medicine',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('nurse_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('contact_no', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'Nurse',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patient_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('contact_no', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'Patient',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('prescription_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Prescription',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('procedure_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'Procedure',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_no', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('availability', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Room',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('test_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'Test',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('treatment_id', models.IntegerField(primary_key=True, serialize=False)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('details', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'Treatment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Aftercare',
            fields=[
                ('treatment', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='dbms_app.treatment')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Aftercare',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('doctor', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='dbms_app.doctor')),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
            ],
            options={
                'db_table': 'Appointment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BillDiag',
            fields=[
                ('diagnosis', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='dbms_app.diagnosis')),
            ],
            options={
                'db_table': 'Bill_Diag',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Consists',
            fields=[
                ('procedure', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='dbms_app.procedure')),
            ],
            options={
                'db_table': 'Consists',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DiagPresc',
            fields=[
                ('diagnosis', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='dbms_app.diagnosis')),
            ],
            options={
                'db_table': 'Diag_Presc',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DoneIn',
            fields=[
                ('treatment', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='dbms_app.treatment')),
            ],
            options={
                'db_table': 'Done_In',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Implies',
            fields=[
                ('diagnosis', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='dbms_app.diagnosis')),
            ],
            options={
                'db_table': 'Implies',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Includes',
            fields=[
                ('medicine', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='dbms_app.medicine')),
                ('unit', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Includes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Involves',
            fields=[
                ('diagnosis', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='dbms_app.diagnosis')),
                ('results', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'Involves',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MedicalBill',
            fields=[
                ('prescription', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='dbms_app.prescription')),
            ],
            options={
                'db_table': 'Medical_Bill',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PatientLog',
            fields=[
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='dbms_app.patient')),
                ('checkin', models.DateTimeField()),
                ('checkout', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Patient_Log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pays',
            fields=[
                ('patient_id', models.IntegerField()),
                ('bill_number', models.OneToOneField(db_column='bill_number', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='dbms_app.bill')),
            ],
            options={
                'db_table': 'Pays',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Performs',
            fields=[
                ('treatment', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='dbms_app.treatment')),
            ],
            options={
                'db_table': 'Performs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Recommends',
            fields=[
                ('diagnosis', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='dbms_app.diagnosis')),
            ],
            options={
                'db_table': 'Recommends',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Serves',
            fields=[
                ('treatment', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='dbms_app.treatment')),
            ],
            options={
                'db_table': 'Serves',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Treated',
            fields=[
                ('treatment', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='dbms_app.treatment')),
            ],
            options={
                'db_table': 'Treated',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TreatmentBill',
            fields=[
                ('treatment', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='dbms_app.treatment')),
            ],
            options={
                'db_table': 'Treatment_Bill',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TreatmentPresc',
            fields=[
                ('treatment', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='dbms_app.treatment')),
            ],
            options={
                'db_table': 'Treatment_Presc',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Undergoes',
            fields=[
                ('diagnosis', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='dbms_app.diagnosis')),
            ],
            options={
                'db_table': 'Undergoes',
                'managed': False,
            },
        ),
    ]
