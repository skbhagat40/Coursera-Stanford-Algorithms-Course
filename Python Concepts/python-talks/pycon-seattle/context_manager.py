from contextlib import contextmanager
from sqlite3 import connect


# let's setup a context manager Temptable

# let's implement a context manager and temptable as a function
@contextmanager # makes life easier
def temptable(cur):
    cur.execute('create table points(x int, y int)')
    yield
    cur.execute('drop table points')


# refactor to remove hardcoded generator
class contextmanager:
    def __init__(self, gen):
        self.gen = gen

    def __call__(self, *args, **kwargs):
        self.args, self.kwargs = args, kwargs
        return self

    def __enter__(self):
        self.gen_inst = self.gen(*self.args, **self.kwargs)
        next(self.gen_inst)

    def __exit__(self, exc_type, exc_val, exc_tb):
        next(self.gen_inst, None)


# temptable = contextmanager(temptable) can be commented when using decorator.

with connect('test.db') as conn:
    cursor = conn.cursor()
    with temptable(cursor):
        cursor.execute('insert into points(x, y) values (1, 2)')
        query = "select * from points"
        cursor.execute(query)
        row = cursor.fetchall()
        print('row', row)
