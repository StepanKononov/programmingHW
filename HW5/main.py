class mydefaultdict(dict):
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.update(*args, **kwargs)

    def __getitem__(self, key):
        if key in self:
            return dict.__getitem__(self, key)
        else:
            dict.__setitem__(self, key, self.func())
            return dict.__getitem__(self, key)


