def test_home_page(client):
    """Test the ask endpoint."""
    response = client.get('/ask')
    assert response.status_code == 200
