from time import sleep


class DataBaseConnection:
    def __init__(self):
        self.data = []

    def get_data(self):
        for i in range(10):
            sleep(0.5)
            self.data.append(i)
        return self.data


db_con = DataBaseConnection()


# for data in db_con.get_data():
#     print("data is {}".format(data))

# so in the above code we had to wait for 5 seconds and
# spend 10 units of storage for event to get the first byte of data.
# This can get more cumbersome if we have large no. of data and in certain cases we
# might not even need them.

# So, generators come to our rescue.

# Going back to our data model method we have __iter__ and __next__ protocols for implementing generators.

# So, we can rewrite our code as follows.

class DataBaseConnection:
    def __init__(self):
        self.rv = 0
        self.data = []

    def __iter__(self):
        return self

    def __next__(self):
        sleep(0.5)
        self.rv += 1
        if self.rv == 10:
            raise StopIteration
        return self.rv
    # def get_data(self):
    #     for i in range(10):
    #         sleep(0.5)
    #         self.data.append(i)
    #     return self.data


db_con = DataBaseConnection()

for data in db_con:
    print("data is {}".format(data))

# In this case the operation is non blocking. Saves us time and space.
