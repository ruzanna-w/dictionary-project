from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class EnglishWords(models.Model):
    english_word = models.CharField(max_length=255)
    word_difficulty = models.CharField(max_length=255)

class UserDictionary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    eng_word = models.ForeignKey(EnglishWords, on_delete=models.CASCADE)
    added_at = models.DateField()

class Translations(models.Model):
    eng_word = models.ForeignKey(EnglishWords, on_delete=models.CASCADE)
    russian_word = models.CharField(max_length=255)

class WordStatistic(models.Model):
    user_dictionary = models.ForeignKey(UserDictionary, on_delete=models.CASCADE)
    count_correct_word = models.IntegerField()
    count_incorrect_word = models.IntegerField()
    last_practiced = models.DateField()