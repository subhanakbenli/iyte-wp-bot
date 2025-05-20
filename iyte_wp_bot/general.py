from bus.models import Bus, Trip

def ekle_otobus_seferleri(bus_number, route_data, station1="IYTE", station2="Urla"):
    """
    route_data = {
        "Weekday": {
            "from_station1": [...],  # station1 -> station2 saatleri
            "from_station2": [...],  # station2 -> station1 saatleri
        },
        "Saturday": {
            "from_station1": [...],
            "from_station2": [...],
        },
        "Sunday": {
            "from_station1": [...],
            "from_station2": [...],
        }
    }
    """

    bus, _ = Bus.objects.get_or_create(number=bus_number)

    def add_trips(departure_list, is_start_from_iyte, trip_day, departure_station, arrival_station):
        for dep_time in departure_list:
            Trip.objects.create(
                bus=bus,
                trip_day=trip_day,
                is_start_from_iyte=is_start_from_iyte,
                departure_station=departure_station,
                arrival_station=arrival_station,
                departure_time=dep_time,
            )

    for day in route_data:
        # station1 -> station2 (ör: İYTE -> Urla)
        add_trips(
            departure_list=route_data[day]["from_station1"],
            is_start_from_iyte=True,
            trip_day=day,
            departure_station=station1,
            arrival_station=station2
        )
        # station2 -> station1 (ör: Urla -> İYTE)
        add_trips(
            departure_list=route_data[day]["from_station2"],
            is_start_from_iyte=False,
            trip_day=day,
            departure_station=station2,
            arrival_station=station1
        )

# ÖRNEK KULLANIM: 882 numaralı otobüs için
route_882 = {
    "Weekday": {
        "from_station1": [
            "07:20", "08:05", "08:50", "09:35", "10:20", "11:05", "11:50", "12:40", "13:30",
            "14:20", "15:10", "16:00", "16:50", "17:40", "18:30", "19:20", "20:00", "20:40",
            "21:20", "22:40", "00:00"
        ],
        "from_station2": [
            "06:30", "07:20", "08:05", "08:50", "09:35", "10:20", "11:05", "11:50", "12:40",
            "13:30", "14:20", "15:10", "16:00", "16:50", "17:40", "18:30", "19:20", "20:00",
            "20:40", "22:00", "23:20"
        ]
    },
    "Saturday": {
        "from_station1": [
            "07:20", "08:05", "08:50", "09:35", "10:20", "11:05", "11:50", "12:40", "13:30",
            "14:20", "15:10", "16:00", "16:50", "17:40", "18:30", "19:20", "20:00", "20:40",
            "21:20"
        ],
        "from_station2": [
            "06:30", "07:20", "08:05", "08:50", "09:35", "10:20", "11:05", "11:50", "12:40",
            "13:30", "14:20", "15:10", "16:00", "16:50", "17:40", "18:30", "19:20", "20:00",
            "20:40"
        ]
    },
    "Sunday": {
        "from_station1": [
            "07:20", "08:05", "08:50", "09:35", "10:20", "11:05", "11:50", "12:40", "13:30",
            "14:20", "15:10", "16:00", "16:50", "17:40", "18:30", "19:20", "20:00", "20:40",
            "21:20"
        ],
        "from_station2": [
            "06:30", "07:20", "08:05", "08:50", "09:35", "10:20", "11:05", "11:50", "12:40",
            "13:30", "14:20", "15:10", "16:00", "16:50", "17:40", "18:30", "19:20", "20:00",
            "20:40"
        ]
    }
}

# Fonksiyonu çağırıyoruz:
ekle_otobus_seferleri("882", route_882, station1="IYTE", station2="Urla")
