

def add_records(records):
    land_data = open("../../resources/land_data.csv", "a")
    land_data.writelines(records)
    land_data.close()


def read_records():
    land_data = open("../../resources/land_data.csv", "a")
    all_records = land_data.readlines()
    land_data.close()
    return all_records
