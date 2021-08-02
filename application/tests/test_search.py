import json
from app import app
from utils.json_tree_query import convert_query
app.testing = True
client = app.test_client()
def test_simple_get():
    res = client.get('/students')
    assert len(res.json) >= 1

    res = client.get('/stream')
    assert len(res.json) >= 31


def test_get_student_with_id():
    res = client.get('/students/1')
    print({ 'student': res})
    assert len(res.json) >= 1

def test_get_stream_with_id():

    res = client.get('/stream/1')
    print({ 'stream': res})
    assert len(res.json) >= 1
