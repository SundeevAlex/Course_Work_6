# Generated by Django 4.2.2 on 2024-07-09 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('email', models.EmailField(max_length=100, verbose_name='Электронная почта')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время попытки отправки')),
                ('status', models.CharField(choices=[('Успешно', 'Успешно'), ('Неуспешно', 'Неуспешно')], max_length=50, verbose_name='Cтатус рассылки')),
                ('server_response', models.CharField(blank=True, max_length=150, null=True, verbose_name='Ответ сервера почтового сервиса')),
            ],
            options={
                'verbose_name': 'Попытка рассылки',
                'verbose_name_plural': 'Попытки рассылки',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Тема')),
                ('message', models.TextField(verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('description', models.TextField(blank=True, help_text='необязательное поле', null=True, verbose_name='Описание')),
                ('status', models.CharField(choices=[('Завершена', 'Завершена'), ('Создана', 'Создана'), ('Запущена', 'Запущена')], default='Создана', max_length=150, verbose_name='Статус')),
                ('periodicity', models.CharField(choices=[('Раз в день', 'Раз в день'), ('Раз в неделю', 'Раз в неделю'), ('Раз в месяц', 'Раз в месяц')], default='Раз в день', max_length=150, verbose_name='Периодичность')),
                ('start_date', models.DateTimeField(blank=True, help_text='(формат дд.мм.гггг) необязательное поле', null=True, verbose_name='Дата начала')),
                ('end_date', models.DateTimeField(blank=True, help_text='необязательное поле', null=True, verbose_name='Дата окончания')),
                ('next_send_time', models.DateTimeField(blank=True, null=True, verbose_name='Время следующей отправки')),
                ('clients', models.ManyToManyField(related_name='mailing', to='mailing.client', verbose_name='Клиенты для рассылки')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
                'ordering': ('name',),
                'permissions': [('deactivate_mailing', 'Can deactivate mailing'), ('view_all_mailings', 'Can view all mailings')],
            },
        ),
    ]
