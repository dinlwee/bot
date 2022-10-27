from django.db import models


class Person(models.Model):
    chat_id = models.PositiveIntegerField("chat id")
    sex = models.PositiveIntegerField(verbose_name="Стать", choices=[(1, "Woman"), (2, "Men")])
    city = models.CharField(verbose_name="Місто", max_length=200)


class ItemsSet(models.Model):
    min_temp = models.FloatField("Мінімальна температура")
    max_temp = models.FloatField("Максимальна температура")
    sex = models.PositiveIntegerField(verbose_name="Стать", choices=[(1, "Жінка"), (2, "Чоловік")])
    wind = models.IntegerField("Швідкість вітру")
    rain = models.IntegerField("Інтенсівнисть дощу")


class Item(models.Model):
    set = models.ForeignKey(ItemsSet, models.CASCADE)
    image = models.ImageField("Картинка")

    





