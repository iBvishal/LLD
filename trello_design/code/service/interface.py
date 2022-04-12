import abc

class basicInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def create(self, **kwargs):
        raise NotImplementedError

    @abc.abstractmethod
    def update(self,  **kwargs):
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self,  **kwargs):
        raise NotImplementedError