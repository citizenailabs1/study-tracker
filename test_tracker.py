from tracker import track_study_time


def test_track_study_time_returns_topic_and_hours():
    result = track_study_time("Python basics", 2)
    assert result == {"topic": "Python basics", "hours": 2}