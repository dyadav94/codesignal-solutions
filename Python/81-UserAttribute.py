class User(object):
    def __init__(self, username, _id, xp, name):
        self.username = username
        self._id = _id
        self.xp = xp
        self.name = name

    def __getattr__(self,item):        
        self.__dict__[item] = ''.join([item,' attribute is not defined'])
        return self.__dict__[item]
    
        


def userAttribute(attribute):
    user = User("annymaster", "1234567", "1500", "anny")
    return getattr(user, attribute)
