from bus.models import Bus, Trip

def ekle_otobus_seferleri(bus_number, route_data, station1="İYTE", station2="Urla"):
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

    def add_trips(departure_list, is_start_from_IYTE, trip_day, departure_station, arrival_station):
        for dep_time in departure_list:
            Trip.objects.update_or_create(
                bus=bus,
                trip_day=trip_day,
                is_start_from_iyte=is_start_from_IYTE,
                departure_station=departure_station,
                arrival_station=arrival_station,
                departure_time=dep_time,
            )

    for day in route_data:
        # station1 -> station2 (ör: İYTE -> Urla)
        add_trips(
            departure_list=route_data[day]["from_station1"],
            is_start_from_IYTE=True,
            trip_day=day,
            departure_station=station1,
            arrival_station=station2
        )
        # station2 -> station1 (ör: Urla -> İYTE)
        add_trips(
            departure_list=route_data[day]["from_station2"],
            is_start_from_IYTE=False,
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
route_883 = {
    "Weekday": {
        "from_station1": [
            "06:35", "07:35", "08:50", "09:18", "09:55", "11:05", "12:20", "13:40",
            "15:00", "15:40", "16:20", "17:30", "18:30", "19:00", "20:30", "21:35", "22:35"
        ],
        "from_station2": [
            "06:35", "07:35", "08:08", "08:40", "09:55", "11:10", "12:15", "13:40",
            "15:00", "16:20", "17:00", "17:10", "17:40", "19:00", "20:20", "21:35", "22:35"
        ]
    },
    "Saturday": {
        "from_station1": [
            "07:20", "08:30", "09:35", "10:45", "11:55", "13:00", "14:10", "15:15",
            "16:25", "17:30", "18:35", "19:50", "20:55", "22:00"
        ],
        "from_station2": [
            "07:20", "08:35", "09:40", "10:45", "11:55", "13:00", "14:10", "15:15",
            "16:25", "17:35", "18:40", "19:45", "20:55", "22:00"
        ]
    }}

route_981 = {
    "Weekday": {
        "from_station1": [  # BALIKLIOVA Kalkış
            "06:30","08:30","10:30","21:00","22:30"   
        ],
        "from_station2": [  # F.ALTAY AKT. Kalkış
            "06:45","08:30","12:30","19:00",
            "20:30",  # Bisiklet aparatı var
            "23:00"
        ]
    },
    "Saturday": {
        "from_station1": [
            "06:30","08:15","19:40","21:30"  
        ],
        "from_station2": [
            "06:45","08:15","17:45","19:40","21:30"
        ]
    },
    "Sunday": {
        "from_station1": [
            "06:30","08:15","19:40","21:30" 
        ],
        "from_station2": [
            "06:45","08:15","17:45","19:40","21:30"
        ]
    }
}
route_982 = {
    "Weekday": {
        "from_station1": [
            "06:15", "08:45", "10:40", "12:20", "14:00", "15:40", "17:20", "19:00"
        ],
        "from_station2": [
            "07:00", "07:45", "10:40", "12:20", "14:00", "15:40", "17:20"
        ]
    },
    "Saturday": {
        "from_station1": [
            "10:15", "11:45", "13:15", "14:45", "16:15", "17:45"
        ],
        "from_station2": [
            "10:15", "11:45", "13:15", "14:45", "16:15"
        ]
    },
    "Sunday": {
        "from_station1": [
            "10:15", "11:45", "13:15", "14:45", "16:15", "17:45"
        ],
        "from_station2": [
            "10:15", "11:45", "13:15", "14:45", "16:15"
        ]
    }
}

route_760 = {
    "Weekday": {
        "from_station1": [  # ÇEŞME Kalkış
            "06:00", "06:45", "07:30", "08:15", "09:45", "10:30", "11:15", "12:45",
            "13:30", "14:15", "15:00", "15:45", "16:30", "17:15", "18:45", "19:30", "20:15"
        ],
        "from_station2": [  # URLA Kalkış
            "06:00", "06:45", "07:30", "08:15", "09:00", "09:45", "11:15", "12:00",
            "12:45", "14:15", "15:00", "15:45", "16:30", "17:15", "18:00", "18:45", "20:15"
        ]
    },
    "Saturday": {
        "from_station1": [
            "06:30", "07:30", "08:30", "09:30", "10:30", "11:30", "12:30", "13:30",
            "14:30", "15:30", "16:30", "17:30", "18:30", "19:30", "20:30"
        ],
        "from_station2": [
            "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00",
            "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00"
        ]
    },
    "Sunday": {
        "from_station1": [
            "06:30", "07:30", "08:30", "09:30", "10:30", "11:30", "12:30", "13:30",
            "14:30", "15:30", "16:30", "17:30", "18:30", "19:30", "20:30"
        ],
        "from_station2": [
            "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00",
            "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00"
        ]
    }
}
route_761 = {
    "Weekday": {
        "from_station1": [  # KARABURUN Kalkış
            "06:00", "08:00", "09:00", "10:00", "14:00", "17:00", "18:00", "19:00", "20:00"
        ],
        "from_station2": [  # URLA Kalkış
            "06:00", "07:00", "08:00", "12:00", "15:00", "16:00", "17:00", "18:00", "20:00"
        ]
    },
    "Saturday": {
        "from_station1": [
            "06:00", "08:00", "09:00", "10:00", "14:00", "17:00", "18:00", "20:00"
        ],
        "from_station2": [
            "06:00", "07:00", "08:00", "12:00", "15:00", "16:00", "18:00", "20:00"
        ]
    },
    "Sunday": {
        "from_station1": [
            "06:25", "10:25", "14:25", "18:25"
        ],
        "from_station2": [
            "08:25", "12:25", "16:25", "20:25"
        ]
    }
}

# Fonksiyonu çağırıyoruz:
def saatleri_guncelle():
    ekle_otobus_seferleri("882", route_882, station1="İYTE", station2="Urla")
    ekle_otobus_seferleri("883", route_883, station1="İYTE", station2="İzmir")
    ekle_otobus_seferleri("981", route_981, station1="BALIKLIOVA", station2="İzmir")
    ekle_otobus_seferleri("982", route_982, station1="İYTE", station2="İzmir")
    ekle_otobus_seferleri("760", route_760, station1="Çeşme", station2="Urla")
    ekle_otobus_seferleri("761", route_761, station1="Karaburun", station2="Urla")
    
