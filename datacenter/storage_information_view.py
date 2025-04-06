from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.models import get_duration
from datacenter.models import format_duration
from django.shortcuts import render




def storage_information_view(request):
    # Программируем здесь
    names = []
    duration_session = []
    entry_times = []
    visits = Visit.objects.filter(leaved_at=None)
    for visit in visits:
        duration = get_duration(visit)
        session_duration = format_duration(duration)
        name = str(visit.passcard)
        time = str(visit.entered_at)
        names.append(name)
        entry_times.append(time)
        duration_session.append(session_duration)



    non_closed_visits = [{"who_entered": a, 'entered_at': b, 'duration': c} for a, b, c in zip(names, entry_times, duration_session)]
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
            
            