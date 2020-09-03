from collections import OrderedDict
import constraints as con
import datetime
import random
import binascii

desk_location_order_map = {
            "LocationID": 1,
            "Building": 2,
            "Floor": 3,
            "Location": 4,
            "Type": 5,
            "Division": 6,
            "Department": 7,
            "Category 1": 8,
            "Category 2": 9,
            "Category 3": 10
}

desk_data_order_map = {
            "#": 1,
            "Taken": 2,
            "By": 3,
            "LocationID Desk": 4,
            "Code": 5,
            "Result": 6,
            "Detail": 7,
            "Slot": 8,
            "Start": 9, #comment
}


def generate_desk_locations():
    div_count = len(con.divisions) - 1
    desk_locations = []
    const_hash = binascii.crc32(str(datetime.datetime.now()).encode('utf-8'))

    for building in con.buildings:
        tmp = [{
            "LocationID": f'{building}_{const_hash}_{i}',
            "Building": building,
            "Floor": random.randint(1, con.floors_qty),
            "Location": "some location",
            "Type": "DESK",
            "Division": con.divisions[random.randint(0, div_count)],
            "Department": f"dep_{i}",
            "Category 1": f"cat_{i}",
            "Category 2": f"cat_{i}",
            "Category 3": f"cat_{i}"
        } for i in range(con.desk_location_count_per_building)]
        desk_locations += tmp

    return [OrderedDict(sorted(i.items(), key=lambda x: desk_location_order_map[x[0]])) for i in desk_locations]


def generate_desk_data(desk_locations):
    desk_data = []
    result_count = len(con.results) - 1
    const_hash = binascii.crc32(str(datetime.datetime.now()).encode('utf-8'))
    increment = 0
    date = datetime.datetime.strptime(con.start_date, '%d-%m-%Y')

    for location in desk_locations:
        for day in range(5):
            tmp = [{
                "#": f'{const_hash}_{increment+hour}',
                "Taken": date + datetime.timedelta(days=day, hours=hour),
                "By": 'botrak',
                "LocationID Desk": location.get('LocationID'),
                "Code": 5871,
                "Result": con.results[random.randint(0, result_count)],
                "Detail": None,
                "Slot": 22789,
                "Start": (date + datetime.timedelta(days=day, hours=hour)).strftime("%Y-%m-%d %H:%M"),
            } for hour in [9, 10, 11, 12, 13, 14, 15, 16, 17]]
            desk_data += tmp
            increment += 1

    return [OrderedDict(sorted(i.items(), key=lambda x: desk_data_order_map[x[0]])) for i in desk_data]
