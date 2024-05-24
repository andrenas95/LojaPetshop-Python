from hashlib import new
import pytest
from rest_framework.test import APIClient

new
@pytest.mark.django_db
def test_todos_petshop():
    client = APIClient()
    response = client.get('/api/petshop')
    assert len(response.data[results]) == 0