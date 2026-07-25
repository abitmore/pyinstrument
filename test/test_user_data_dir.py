from pyinstrument.util import _user_data_dir

from .appdirs import user_data_dir


def test_user_data_dir_matches_appdirs():
    assert _user_data_dir() == user_data_dir("pyinstrument", "com.github.joerick")
