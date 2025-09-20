import requests

def test_homepage():
    url = "http://localhost/index.html"
    response = requests.get(url)

    # Basic checks
    assert response.status_code == 200

    # Content checks
    assert "welcoe to pipeline pracise pradise" in response.text
    assert "Hello World from Jenkins!" in response.text
    assert "If you see this, your web server is working!" in response.text

    print("✅ Test passed: IIS site deployed and verified!")

if __name__ == "__main__":
    test_homepage()
