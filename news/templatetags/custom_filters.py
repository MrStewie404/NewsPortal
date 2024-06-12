from django import template
register = template.Library()
from news.models import User

CENSOR_WORDS = "киберспортивный".split()

@register.filter()
def preview_title(text):
    return f"{text[:20]}..."

@register.filter()
def preview_text(text):
    return f"{text[:124]}..."

@register.filter()
def date_publicate(date):
    date = f'{date}'[:10].split('-')
    return f"{date[2]}.{date[1]}.{date[0]}"

@register.filter()
def author_username(id):
    return User.objects.filter(id=id)[0].username

@register.filter()
def censor(text):
    censored_text = []
    for word in text.split():
        if word.lower() in CENSOR_WORDS:
            censored_text.append(f"{word[0]}{'*'*len(word)}")
        else:
            censored_text.append(word)
    return " ".join(censored_text)