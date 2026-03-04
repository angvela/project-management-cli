from models.user import User


def test_add_project():
    user = User("Alex")
    user.add_project("Test Project")
    assert len(user.projects) == 1