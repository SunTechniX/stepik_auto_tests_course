import pytest


@pytest.fixture(scope="class")
def prepare_faces():
    print("^_^ [1]", "\n")
    yield
    print(":3 [5]", "\n")


@pytest.fixture()
def very_important_fixture():
    print(":) [3]", "\n")


@pytest.fixture(autouse=True)
def print_smiling_faces():
    print(":-Р [2/4]", "\n")


class TestPrintSmilingFaces():
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        # какие-то проверки
        pass

    def test_second_smiling_faces(self, prepare_faces):
        # какие-то проверки
        pass
