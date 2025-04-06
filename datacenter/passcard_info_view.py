from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.models import get_duration
from datacenter.models import format_duration
from datacenter.models import is_visit_long
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    entry_times = []
    duration_session = []
    is_strange = []
    obj = get_object_or_404(Passcard, passcode=passcode)
    passcard = Visit.objects.filter(passcard=obj)
    for visit in passcard:
        duration = get_duration(visit)
        session_duration = format_duration(duration)
        time = str(visit.entered_at)
        strange = is_visit_long(visit, minutes=60)
        entry_times.append(time)
        duration_session.append(session_duration)
        is_strange.append(strange)

    this_passcard_visits = [{'entered_at': a, 'duration': b, 'is_strange': c } for a, b, c in zip(entry_times, duration_session, is_strange)]
    context = {
        'passcard': obj,
        'this_passcard_visits': this_passcard_visits
    }  
    return render(request, 'passcard_info.html', context)

     