# Generated by Django 4.1.4 on 2022-12-20 11:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('noticia', '0002_alter_comentario_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='autor',
            field=models.ForeignKey(auto_created=True, on_delete=django.db.models.deletion.CASCADE, related_name='autor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='post',
            field=models.ForeignKey(auto_created=True, on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='noticia.noticia'),
        ),
    ]