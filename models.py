from peewee import (BooleanField, CharField, IntegerField,
                    IntegrityError, Model, SqliteDatabase)

DATABASE = SqliteDatabase('people.db')


class Person(Model):
    name = CharField(unique=True)
    age = IntegerField()
    location = CharField()
    details = CharField()
    languages = CharField()
    look_for = CharField()
    answer_back = BooleanField(default=False)
    keywords = CharField()

    class Meta:
        database = DATABASE

    @classmethod
    def create_person(
            cls, name, age, location, details=None, languages=None,
            look_for=None,
            answer_back=False, keywords=None):
        """Creates People using peewee's built-in
        transaction method. If an exception occurs
        within the DATABASE.transaction() block, the transaction will
        be rolled back. Otherwise the people will be committed at
        the end of the block.
        - Peewee Docs
        """
        try:
            with DATABASE.transaction():
                cls.create(
                    name=name,
                    age=age,
                    location=location,
                    details=details,
                    languages=languages,
                    look_for=look_for,
                    answer_back=answer_back,
                    keywords=None,
                )
        except IntegrityError:
            raise ValueError('Person already exsists in database.')

    def __str__(self):
        return "Name: {} \nAge: {} \nCity: {}".format(
            self.name, self.age, self.city)


class ViewedPerson(Model):
    name = CharField(unique=True)

    class Meta:
        database = DATABASE

    @classmethod
    def create_viewed_person(cls, name):
        try:
            with DATABASE.transaction():
                cls.create(
                    name=name,
                )
        except IntegrityError:
            raise ValueError('Person already exsists in database.')


def initialize():
    """Makes a connection to the ledger.db database, creates the
    neccessary tables if they do not exist, and promptly closes the
    connection
    """
    DATABASE.connect()
    DATABASE.create_tables([Person, ViewedPerson], safe=True)
    DATABASE.close()


if __name__ == "__main__":
    initialize()
    try:
        Person.select().where(Person.location == 'San Francisco, CA')
    except Exception as e:
        print(e)
