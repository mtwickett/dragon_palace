import random

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import Http404

from .forms import DrinkForm
from . import utils


FORTUNES = [
    'Do not be afraid of competition.',
    'An exciting opportunity lies ahead of you.',
    'You love peace.',
    'Get your mind set…confidence will lead you on.',
    'You will always be surrounded by true friends.',
    'Sell your ideas-they have exceptional merit.',
    'You should be able to undertake and complete anything.',
    'You are kind and friendly.',
    'You are wise beyond your years.',
    'Your ability to juggle many tasks will take you far.',
    'A routine task will turn into an enchanting adventure.',
    'Beware of all enterprises that require new clothes.',
    'Be true to your work, your word, and your friend.',
    'Goodness is the only investment that never fails.',
    'A journey of a thousand miles begins with a single step.',
    'Forget injuries; never forget kindnesses.',
    'Respect yourself and others will respect you.',
    'A man cannot be comfortable without his own approval.',
    'Always do right. This will gratify some people and astonish the rest.',
    'It is easier to stay out than to get out.',
    'Sing everyday and chase the mean blues away.',
    'You will receive money from an unexpected source.',
    'Attitude is a little thing that makes a big difference.',
    'Plan for many pleasures ahead.',
    'Experience is the best teacher.',
    'You will be happy with your spouse.',
    'Expect the unexpected.',
    'Stay healthy. Walk a mile.',
    'The family that plays together stays together.',
    'Eat chocolate to have a sweeter life.',
    'Once you make a decision the universe conspires to make it happen.',
    'Make yourself necessary to someone.',
    'The only way to have a friend is to be one.',
    'Nothing great was ever achieved without enthusiasm.',
    'Dance as if no one is watching.',
    'Live this day as if it were your last.',
    'Your life will be happy and peaceful.',
    'Reach for joy and all else will follow.',
    'Move in the direction of your dreams.',
    'Bloom where you are planted.',
    'Appreciate. Appreciate. Appreciate.',
    'Happy News is on its way.'
]

# @login_required
def home(request):
    try:
        context = {'fortune': random.choice(FORTUNES)}
        return render(request, 'home_template.html', context)
    except:
        raise Http404('Page does not exist')


# @login_required
def drink(request):
    try:
        form = DrinkForm()
        if request.method == 'POST':
            form = DrinkForm(request.POST)
            if form.is_valid():
                form.save()
        context = {
            'form': form,
            'fortune': random.choice(FORTUNES),
            }
        return render(request, 'drink_template.html', context)
    except:
        raise Http404('Page does not exist')


# @login_required
def calculator(request):
    try:
        context = {'fortune': random.choice(FORTUNES)}
        return render(request, 'calculator_template.html', context)
    except:
        Http404('Page does not exist')



