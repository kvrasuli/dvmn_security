from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    non_closed_visits_query = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in non_closed_visits_query:
        non_closed_visits.append(
            {
                "who_entered": visit.passcard.owner_name,
                "entered_at": visit.entered_at,
                "duration": visit.format_duration(visit.get_duration()),
            }
        )

    context = {
        "non_closed_visits": non_closed_visits,  # незакрытые посещения
    }
    return render(request, 'storage_information.html', context)
