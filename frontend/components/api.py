import requests

BASE_URL = "http://127.0.0.1:8000"


def health():
    return requests.get(
        f"{BASE_URL}/health"
    ).json()


def upload(files):

    response = requests.post(
        f"{BASE_URL}/ingest/",
        files=files,
    )

    return response.json()


def generate(
    subject,
    topic,
    difficulty,
    number_of_questions,
):

    response = requests.post(
        f"{BASE_URL}/generate/test",
        json={
            "subject": subject,
            "topic": topic,
            "difficulty": difficulty,
            "number_of_questions": number_of_questions,
        },
    )

    return response.json()