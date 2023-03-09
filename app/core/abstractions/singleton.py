# -*- coding: utf-8 -*-
from abc import abstractmethod


class SingletonClass:
    """[summary]
    """
    def __new__(cls, *args, **kwargs) -> object:
        """control singleton create instance
        Returns:
            object -- instance of class
        """
        if not hasattr(cls, '_singleton_instance') or not cls._singleton_instance:
            cls._singleton_instance = super().__new__(cls)
        return cls._singleton_instance

    def __init__(self, **kwargs):
        """singleton init
        """
        if not hasattr(self, '_singleton_init_done'):
            self._singleton_init(**kwargs)
            self._singleton_init_done = True    # this make sure init start only 1 times
            return

    @abstractmethod
    def _singleton_init(self, **kwargs):
        """You must overide this method
        """
        raise NotImplementedError
