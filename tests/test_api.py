def test_list_records(client):
    response = client.get('/list')
    assert response.status_code == 200
    assert 'Ali Veli'.encode('utf-8') in response.data
    assert 'Fatma Yılmaz'.encode('utf-8') in response.data

def test_add_record(client):
    response = client.post('/add', data={"name": "Mehmet Tester", "email": "mehmet@test.com"})
    assert response.status_code == 302
    response2 = client.get('/list')
    assert 'Mehmet Tester'.encode('utf-8') in response2.data

def test_delete_record(client):
    response = client.post('/delete/1', follow_redirects=True)
    assert response.status_code in (200, 302)
    response2 = client.get('/list')
    page_str = response2.data.decode('utf-8')
    print("List page after delete:", page_str)
    assert 'Ali Veli' not in page_str