

import scorer
from scorer import calculate_score
import pytest
import requests


# custom class to be the mock return value of requests.get()
class MockResponse:
    months = ""

    @staticmethod
    def json():
        return {"flowering_months": MockResponse.months.split(",")}


@pytest.fixture
def mock_all_month_response(monkeypatch):
    """Requests.get() mocked to return {'mock_key':'mock_response'}."""
    def mock_get(*args, **kwargs):
        response = MockResponse
        response.months = "may,june,july,august"
        return MockResponse
    monkeypatch.setattr(requests, "get", mock_get)


@pytest.fixture
def mock_few_month_response(monkeypatch):
    """Requests.get() mocked to return {'mock_key':'mock_response'}."""
    def mock_get(*args, **kwargs):
        response = MockResponse
        response.months = "may,june"
        return MockResponse
    monkeypatch.setattr(requests, "get", mock_get)

def test_calculate_score_no_flowers_in_garden():
    flowers = []
    garden_size = "small"
    assert calculate_score(garden_size, flowers) == "Our furry flying friends will be disappointed! You should plant some more flowers in your small garden."


def test_top_marks(mock_all_month_response):
    garden_size = "large"
    flowers = ["daisy"]
    score = calculate_score(garden_size, flowers)
    assert score == "Top marks! Bees love your large garden."


def test_calculate_score_no_late_blooming_flowers_in_garden(mock_few_month_response):
    flowers = ["azalea", "rhododendron"]
    garden_size = "small"
    score = calculate_score(garden_size, flowers)
    assert score == "Good work! Your garden would be even more friendly if you planted some flowers that bloom in July and August"


def test_calculate_windowbox():
    garden_size = "windowbox"
    flowers = ["peony", "giant_daisy"]
    score = calculate_score(garden_size, flowers)
    assert score == "Top marks! Bees love your windowbox."
