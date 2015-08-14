"""A Three-D vector library written as part of a 
computational physics course."""

from .vector import Threevec
from .vector import i, j, k
from .vector import recvec
from .vector import cylvec
from .vector import sphvec

__all__ = ['Threevec',
           'i',
           'j',
           'k',
           'recvec',
           'cylvec',
           'sphvec']
