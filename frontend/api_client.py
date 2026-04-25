import os
import requests

API_URL = os.getenv("API_URL", "http://localhost:8080")


class APIError(Exception):
    pass


def _headers(token: str) -> dict:
    return {"Authorization": f"Bearer {token}"}


def _check(r: requests.Response) -> dict:
    if not r.ok:
        try:
            msg = r.json().get("error", r.text)
        except Exception:
            msg = r.text
        raise APIError(msg)
    return r.json()


# Auth

def login(email: str, password: str) -> dict:
    return _check(requests.post(f"{API_URL}/auth/login", json={"email": email, "password": password}))


def register(email: str, password: str) -> dict:
    return _check(requests.post(f"{API_URL}/auth/register", json={"email": email, "password": password}))


# Food

def log_food(token: str, description: str, calories: int, carb_grams: float,
             protein_grams: float, fat_grams: float, timestamp: str) -> dict:
    return _check(requests.post(f"{API_URL}/food", headers=_headers(token), json={
        "description": description,
        "calories": calories,
        "carb_grams": carb_grams,
        "protein_grams": protein_grams,
        "fat_grams": fat_grams,
        "timestamp": timestamp,
    }))


def get_food(token: str, start: str = None, end: str = None) -> list:
    params = {k: v for k, v in {"start": start, "end": end}.items() if v}
    return _check(requests.get(f"{API_URL}/food", params=params, headers=_headers(token)))


# Exercise

def log_exercise(token: str, description: str, calories: int, duration_minutes: int, timestamp: str) -> dict:
    return _check(requests.post(f"{API_URL}/exercise", headers=_headers(token), json={
        "description": description,
        "calories": calories,
        "duration_minutes": duration_minutes,
        "timestamp": timestamp,
    }))


def get_exercise(token: str, start: str = None, end: str = None) -> list:
    params = {k: v for k, v in {"start": start, "end": end}.items() if v}
    return _check(requests.get(f"{API_URL}/exercise", params=params, headers=_headers(token)))


# Weight

def log_weight(token: str, weight: float, timestamp: str) -> dict:
    return _check(requests.post(f"{API_URL}/weight", headers=_headers(token), json={
        "weight": weight,
        "timestamp": timestamp,
    }))


def get_weight(token: str, start: str = None, end: str = None) -> list:
    params = {k: v for k, v in {"start": start, "end": end}.items() if v}
    return _check(requests.get(f"{API_URL}/weight", params=params, headers=_headers(token)))
