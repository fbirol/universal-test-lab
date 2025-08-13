from tests.factories import fake_record


def test_list_records(client_and_records):
    client, records = client_and_records
    response = client.get("/list")
    assert response.status_code == 200
    body = response.data.decode("utf-8")
    # İlk iki seed edilen kaydın listede olduğunu kontrol et
    assert records[0].name in body
    assert records[0].email in body
    assert records[1].name in body
    assert records[1].email in body


def test_add_record(client_and_records):
    client, _ = client_and_records
    record = fake_record()
    response = client.post("/add", data=record)
    assert response.status_code == 302
    response2 = client.get("/list")
    body = response2.data.decode("utf-8")
    assert record["name"] in body
    assert record["email"] in body


def test_delete_record(client_and_records):
    client, records = client_and_records
    record_to_delete = records[0]
    response = client.post(f"/delete/{record_to_delete.id}", follow_redirects=True)
    assert response.status_code in (200, 302)
    response2 = client.get("/list")
    body2 = response2.data.decode("utf-8")
    assert record_to_delete.name not in body2
