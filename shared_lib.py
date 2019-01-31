# this is a module.
from datetime import datetime
def calculate_age(birth_year):
    return datetime.today().year - birth_year

# test.
if __name__ == '__main__':
    assert calculate_age(1990) == datetime.today().year - 1990
