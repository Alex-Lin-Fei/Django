import os
from django.utils.timezone import now

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'mysite.settings')

import django

django.setup()

from polls.models import Question, Choice


def populate():
    questions = [
        'Where is the capital of China',
        'How many continents are there in the world',
        'Which of the following is the smallest planet int the solar system'
    ]

    choices = [
        ["Beijing", "Shanghai", "Guangzhou", "Chengdu"],
        ["six", "seven", "eight", "nine"],
        ["earth", "Mercury", "Mars", "Venus"]
    ]

    for q, c in zip(questions, choices):
        question = add_question(q)
        for choice_text in c:
            add_choice(question, choice_text)


def add_question(question_text):
    date = now()
    q = Question.objects.get_or_create(question_text=question_text, pub_date=date)[0]
    q.save()
    return q


def add_choice(question, choice_text):
    c = Choice.objects.get_or_create(question=question, choice_text=choice_text)[0]
    c.save()
    return c


if __name__ == "__main__":
    print("Starting Polls population script...")
    populate()

