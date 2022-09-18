def test_root():
    """Testing root function."""
    from fastapi import FastAPI

    from ai_bundle.app import app

    assert isinstance(app, FastAPI)
