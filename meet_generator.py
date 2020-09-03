from collections import OrderedDict
import constraints as con
import datetime
import random
import binascii

meet_location_order_map = {
            "LocationID Meet": 1,
            "LocationName": 2,
            "Building": 3,
            "Floor": 4,
            "Type": 5,
            "Capacity": 6,
            "Results": 7,
            "Category 1": 8,
            "Category 2": 9,
            "Category 3": 10,
}

meet_data_order_map = {
            "#": 1,
            "Taken": 2,
            "By": 3,
            "LocationID Meet": 4,
            "Code": 5,
            "Result": 6,
            "Detail": 7,
            "Slot": 8,
            "Start": 9,
}


def generate_meet_locations():
    type_count = len(con.meet_type) - 1
    meet_locations = []
    const_hash = binascii.crc32(str(datetime.datetime.now()).encode('utf-8'))

    for building in con.buildings:
        tmp = [{
            "LocationID Meet": f'{building}_{const_hash}_{i}',
            "LocationName": f'{const_hash}_{i}',
            "Building": building,
            "Floor": random.randint(1, con.floors_qty),
            "Type": con.meet_type[random.randint(0, type_count)],
            "Capacity": random.randint(3, 30),
            "Results": 123,
            "Category 1": f"cat_{i}",
            "Category 2": f"cat_{i}",
            "Category 3": f"cat_{i}"
        } for i in range(con.desk_location_count_per_building)]
        meet_locations += tmp

    return [OrderedDict(sorted(i.items(), key=lambda x: meet_location_order_map[x[0]])) for i in meet_locations]


def generate_meet_data(meet_locations):
    meet_data = []
    result_count = len(con.meet_results) - 1
    const_hash = binascii.crc32(str(datetime.datetime.now()).encode('utf-8'))
    increment = 0
    date = datetime.datetime.strptime(con.start_date, '%d-%m-%Y')

    for location in meet_locations:
        for day in range(5):
            tmp = [{
                "#": f'{const_hash}_{increment+hour}',
                "Taken": date + datetime.timedelta(days=day, hours=hour),
                "By": 'botrak',
                "LocationID Meet": location.get('LocationID Meet'),
                "Code": 5871,
                "Result": None,
                "Detail": 'No one' if random.randint(0, 2) == 0 else f"{random.randint(1, location['Capacity'])} people",
                "Slot": 22789,
                "Start": (date + datetime.timedelta(days=day, hours=hour)).strftime("%Y-%m-%d %H:%M"),
            } for hour in [9, 10, 11, 12, 13, 14, 15, 16, 17]]
            meet_data += tmp
            increment += 1

    for i in meet_data:
        i['Result'] = 'Unoccupied (Vacant)' if i['Detail'] == 'No one' else con.meet_results[random.randint(0, result_count)]

    return [OrderedDict(sorted(i.items(), key=lambda x: meet_data_order_map[x[0]])) for i in meet_data]


