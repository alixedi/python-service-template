import pytest

from service.db import create_engine, create_engine, init_db


# @pytest.fixture(scope='module')
# def env():
#     return Env(
#         **{

#         }
#     )

@pytest.fixture(scope='module')
def session(env):
    