import csv
from datetime import datetime

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from word_translation.models import (
    EnglishWords,
    UserDictionary,
    Translations,
    WordStatistic
)

User = get_user_model()


class Command(BaseCommand):
    help = "Import all CSV files separately"

    def handle(self, *args, **options):

        # =========================
        # 1. EnglishWords
        # =========================
        with open("data/english_words.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                EnglishWords.objects.create(
                    english_word=row["english_word"],
                    word_difficulty=row["word_difficulty"]
                )

        # =========================
        # 2. Translations
        # =========================
        with open("data/translations.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                eng_word = EnglishWords.objects.get(
                    english_word=row["english_word"]
                )

                Translations.objects.create(
                    eng_word=eng_word,
                    russian_word=row["russian_word"]
                )

        # =========================
        # 3. UserDictionary
        # =========================
        with open("data/user_dictionary.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                user = User.objects.get(username=row["username"])
                eng_word = EnglishWords.objects.get(
                    english_word=row["english_word"]
                )

                UserDictionary.objects.create(
                    user=user,
                    eng_word=eng_word,
                    added_at=datetime.strptime(row["added_at"], "%Y-%m-%d").date()
                )

        # =========================
        # 4. WordStatistic
        # =========================
        with open("data/word_statistics.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                user = User.objects.get(username=row["username"])
                eng_word = EnglishWords.objects.get(
                    english_word=row["english_word"]
                )

                user_dict = UserDictionary.objects.get(
                    user=user,
                    eng_word=eng_word
                )

                WordStatistic.objects.create(
                    user_dictionary=user_dict,
                    count_correct_word=int(row["count_correct_word"]),
                    count_incorrect_word=int(row["count_incorrect_word"]),
                    last_practiced=datetime.strptime(
                        row["last_practiced"], "%Y-%m-%d"
                    ).date()
                )

        self.stdout.write(self.style.SUCCESS("All CSV files imported successfully"))