"""This module includes database operation class.

Author: xxx@xxx.com
Environment set up tips:
  1) ...
  2) ...
"""
import MySQLdb
from datetime import datetime


def calculate_age(birth_year):
    """Calculate the age for a given birth year.
    
    Args:
      birth_year: Integer indicating the year of birth.
    
    Returns:
      Integer indicating the age.
    """
    return datetime.today().year - birth_year


class Person:
    height = 0.0
    weight = 0.0
    name = ''

    def __init__(self, name, height='', weight=0):
        self.weight = weight
        self.height = height
        self.name = name

    def __str__(self):
        return f'name is {self.name}, height is {self.height}cm, weight is {self.weight}kg'

    def tell_name(self):
        if self.name:
            print(f'Hi my name is {self.name}')
        else:
            print("I don't have a name yet.")


class Employee(Person):
    title = ''
    height = ''

    def __init__(self, name, title, height='', weight=''):
        self.title = title
        super().__init__(name, height, weight)

    def __str__(self):
        person_str = super().__str__()
        employ_str = person_str + '\n' + f'title: {self.title}'
        return employ_str

    def tell_title(self):
        print("Hi I'm a {}".format(self.title))


class SqlException(Exception):
    pass


class MyDataBase:
    server_address = ''
    cursor = None
    database_name = ''
    port = 0
    user = ''
    password = ''

    def __del__(self):
        if self.handler:
            self.handler.close()

    def __init__(self, server_address, user, password, database_name, port=3306):
        self.handler = MySQLdb.connect(host=server_address,  # your host, usually localhost
                                       user=user,  # your username
                                       passwd=password,  # your password
                                       db=database_name)  # name of the data base

    def get_cursor(self):
        return self.__get_cursor()

    def __get_cursor(self):
        # you must create a Cursor object. It will let
        #  you execute all the queries you need
        self.cursor = self.handler.cursor()
        return self.cursor

    def query(self, sql):
        """Query and return results in rows.

        Args:
          sql: SQL string.

        Returns:
           A list containing all the query results.
        """
        # Use all the SQL you like
        self.__get_cursor()
        if not sql:
            raise SqlException('Need a SQL.')

        self.cursor.execute(sql)
        return self.cursor.fetchall()


print(f'the __name__ value is {__name__} in {__file__}')

if __name__ == '__main__':
    the_age = calculate_age(1979)
    print(f'The message from {__file__}. The age is {the_age}')

