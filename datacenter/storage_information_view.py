from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.models import get_duration
from datacenter.models import format_duration
from django.shortcuts import render




def storage_information_view(request):
    # Программируем здесь
    visits = Visit.objects.filter(leaved_at=None)

    non_closed_visits = [
        {
            'who_entered': str(visit.passcard),
            'entered_at': str(visit.entered_at),
            'duration': format_duration(get_duration(visit))
        }
        for visit in visits
    ]

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
            
            