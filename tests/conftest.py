import pytest
from app import create_app, db

@pytest.fixture(scope='module')
def app():
    """
    Create and configure a new app instance for each test.
    """
    app = create_app()
    app.config.update({
        "TESTING": True,  # Set to True during testing
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"  # Use in-memory SQLite for tests
    })

    with app.app_context():
        db.create_all()

    yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture(scope='module')
def client(app):
    """A test client for the app."""
    return app.test_client()
