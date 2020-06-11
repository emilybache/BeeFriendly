from datetime import datetime

from flower_service import create_flower


def test_create_flower():
    now = datetime.strptime('2019-08-01', "%Y-%m-%d")
    flower = create_flower("begonia", now)
    assert flower.name == "begonia"
    assert flower.description is None
    assert flower.flowering_months == "august"
