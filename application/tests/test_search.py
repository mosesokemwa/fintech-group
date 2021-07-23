import json
from app import app
from utils.json_tree_query import convert_query

TEST_QUERY_1 = {"CONTAINS":{"message": "error"}}
TEST_QUERY_2 = {"NOT": {"OR": [{"AND": [{"IS": {"browser": "safari"}},{"IS": {"country": "Germany"}}]},{"CONTAINS": {"message": "stacktrace"}}]}}
def test_simple_search():
    app.testing = True
    client = app.test_client()

    res = client.get('/search/browser/philippines')

    assert len(res.json) == 8

    res = client.get('/search/IE/philippines')

    assert len(res.json) == 31


def test_empty():
    orm_Q = convert_query({})
    assert orm_Q == {}


def test_contains():
    orm_Q = convert_query({"CONTAINS":{"message": "error"}})
    assert orm_Q == "select * from log where message like 'error%%'"


def test_advanced_search():
    app.testing = True
    client = app.test_client()

    res = client.get(f'/advanced/{json.dumps(TEST_QUERY_1)}')

    assert len(res.json) == 0

    res = client.get(f'/advanced/{json.dumps(TEST_QUERY_2)}')

    assert len(res.json) == 100