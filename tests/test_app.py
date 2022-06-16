import pytest
from fastapi import FastAPI
from defiant.App import app

def test_app_creation() -> None:
    assert isinstance(app, FastAPI)