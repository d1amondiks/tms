class Task1D(object):
    x = 3

    def xf(self):
        return self.x


class Task1E(Task1D):
    pass


class Task1B(Task1E):
    x = 1
    pass


class Task1C(Task1B):
    pass


class Task1A(Task1B):
    x = 2
    pass
