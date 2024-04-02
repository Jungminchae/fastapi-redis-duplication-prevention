import time
import requests
from concurrent.futures import ThreadPoolExecutor


def send_vote_request(url_data):
    """투표 요청을 보내는 함수"""
    url, data = url_data  # url과 data를 튜플에서 추출
    response = requests.post(url, json=data)
    return response.json()


url = "http://localhost:8000/votes/"
data = {
    "user_id": 100,
    "candidate_id": 1,
}

with ThreadPoolExecutor(max_workers=5) as executor:
    results = executor.map(send_vote_request, [(url, data) for _ in range(5)])

    for result in results:
        print(result)

time.sleep(1)

url = "http://localhost:8000/votes/distributed-lock/"
data = {
    "user_id": 200,
    "candidate_id": 2,
}
with ThreadPoolExecutor(max_workers=5) as executor:
    results = executor.map(send_vote_request, [(url, data) for _ in range(5)])

    for result in results:
        print(result)
