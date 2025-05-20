from .models import Bus, Trip
from collections import defaultdict
from datetime import datetime
from django.utils import timezone
TRIP_DAY_TR = {
            "Weekday": "Hafta İçi",
            "Saturday": "Cumartesi",
            "Sunday": "Pazar"
        }
def get_schedule_with_busNo(bus_no):
    try:
        trip_day = "Weekday" if datetime.now().weekday() < 5 else "Saturday" if datetime.now().weekday() == 5 else "Sunday"
        bus = Bus.objects.get(number=bus_no)
        trip = Trip.objects.filter(bus=bus, trip_day=trip_day)
        trip_str = format_schedule(trip, TRIP_DAY_TR[trip_day])
        
        return trip_str
    except Bus.DoesNotExist:
        return "Seçili Otobüs bulunamadı."
    except Trip.DoesNotExist:
        return "Seçili Otobüse ait sefer bulunamadı"
    except Exception as e:
        print(f"Error: {e}")
        return "Bir hata oluştu. Lütfen tekrar deneyin."
def get_schedule_with_from_to(from_station, to_station):
    try:
        trip_day = "Weekday" if datetime.now().weekday() < 5 else "Saturday" if datetime.now().weekday() == 5 else "Sunday"
        if from_station == "heryer":
            schedule = Trip.objects.filter(arrival_station=to_station, trip_day=trip_day)
        elif to_station == "heryer":
            schedule = Trip.objects.filter(departure_station=from_station, trip_day=trip_day)
        else:
            schedule = Trip.objects.filter(departure_station=from_station, arrival_station=to_station)

        schedule_str = format_schedule(schedule,TRIP_DAY_TR[trip_day])
        return schedule_str
    except Trip.DoesNotExist:
        return None
    

def format_schedule(schedule,tripday):
    if not schedule:
        return "Sefer bulunamadı."

    now = (timezone.localtime() if hasattr(timezone, 'localtime') else datetime.now()).astimezone(timezone.get_fixed_timezone(180)).time()

    # Otobüs, kalkış ve varışa göre saatleri grupla
    grouped = defaultdict(list)
    for trip in schedule:
        key = (trip.bus.number, trip.departure_station, trip.arrival_station)
        grouped[key].append(trip.departure_time)

    lines = [f"🚌 *{tripday} Sefer Bilgileri* 🚌"]

    for (bus_number, dep, arr), times in grouped.items():
        lines.append(f"*{bus_number}*: *{dep}* ➔ *{arr}* ")
        times = sorted(times)
        for i in range(0, len(times), 4):
            row = []
            for t in times[i:i+4]:
                t_str = t.strftime('%H:%M')
                print(t_str, now)
                if t < now:
                    row.append(f"_{t_str}_") 
                else:
                    row.append(f"*{t_str}*")
            lines.append("   ".join(row))
        lines.append("──────────────")

    return "\n".join(lines)
