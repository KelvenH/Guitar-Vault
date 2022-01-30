from django.db.models import Sum
from .models import MemberProfile


def plectrum_balance(request):
    """
    For loggedin users, calculate the total sum of plectrum tokens (across all purchased membership plans) note this operates along 'reverse' ForeignKey relationships through MemberProfile - Order - Account models to the plectrum_balance field.
    """

    if request.user.is_authenticated:
        user_plec_balance = MemberProfile.objects.filter(user=request.user).aggregate(balance=Sum('orders__accounts__plectrum_balance'))['balance']

    else:
        user_plec_balance = 0

    context = {
        'user_plec_balance': user_plec_balance,
    }

    return context
