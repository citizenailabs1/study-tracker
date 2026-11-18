study_records = []

def track_study_time(topic, hours):
    record = {"topic": topic, "hours": hours}
    study_records.append(record)

track_study_time("Learning Python", 3)
track_study_time("Database Basics", 2)

print(study_records)
