import json
import datetime

def validate_record(record):
    try:
        timestamp = record.get("timestamp")

        truck_id = record.get("truck_id")
        if not truck_id or not isinstance(truck_id, str):
            return False, "Invalid or missing truck_id", timestamp

        latitude = record.get("latitude")
        if not isinstance(latitude, float):
            return False, "Invalid latitude", timestamp

        longitude = record.get("longitude")
        if not isinstance(longitude, float):
            return False, "Invalid longitude", timestamp

        return True, "Valid", timestamp

    except Exception as e:
        return False, f"Exception: {str(e)}", None


def process_log_file(filepath):
    records = []
    with open(filepath, "r") as file:
        records = json.load(file)
    
    header = f"{'Truck ID':<20} {'Timestamp':<30} {'Status':<10} {'Message'}\n"
    
    with open("success.log", "w") as success_log, open("error.log", "w") as error_log:
        success_log.write(header)
        error_log.write(header)

        for record in records:
            valid, message, timestamp = validate_record(record)
            
            if timestamp is None:
                timestamp = "NoTime"
            
            truck_id = record.get("truck_id", "UNKNOWN")
            
            line = f"{truck_id:<20} {timestamp:<30} "

            if valid:
                success_log.write(line + f" {'SUCCESS':<10} {message}\n")
            else:
                error_log.write(line + f" {'ERROR':<10} {message}\n")

process_log_file("log_input.json")
