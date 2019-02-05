"""This is the entry of the program."""

# from shared_lib import first_module
# Another way, with alias.
from shared_lib import first_module as lib


if __name__ == '__main__':
    print(f'the __name__ value is {__name__} in {__file__}')

    the_age = lib.calculate_age(1979)
    print(the_age)

    tom = lib.Employee(name='tom', title='software engineer', height=170, weight=180)
    print(tom)

    db_obj = lib.MyDataBase(database_name='client', server_address='10.198.1.1', user='john', password='password')
    sql = 'Select Id, Name from User order by CreatedDateTime Desc limit 100'
    results = db_obj.query(sql)
