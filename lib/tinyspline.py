# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.0
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError('Python 2.7 or later required')

# Import the low-level C/C++ module
if __package__ or '.' in __name__:
    from . import _tinysplinepython
else:
    import _tinysplinepython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _tinysplinepython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _tinysplinepython.SWIG_PyStaticMethod_New

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if name == "thisown":
        return self.this.own(value)
    if name == "this":
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if not static:
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if name == "thisown":
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


TS_MAX_NUM_KNOTS = _tinysplinepython.TS_MAX_NUM_KNOTS
TS_MIN_KNOT_VALUE = _tinysplinepython.TS_MIN_KNOT_VALUE
TS_MAX_KNOT_VALUE = _tinysplinepython.TS_MAX_KNOT_VALUE
TS_KNOT_EPSILON = _tinysplinepython.TS_KNOT_EPSILON
OPENED = _tinysplinepython.OPENED
CLAMPED = _tinysplinepython.CLAMPED
BEZIERS = _tinysplinepython.BEZIERS
ts_bspline_degree = _tinysplinepython.ts_bspline_degree
ts_bspline_set_degree = _tinysplinepython.ts_bspline_set_degree
ts_bspline_order = _tinysplinepython.ts_bspline_order
ts_bspline_set_order = _tinysplinepython.ts_bspline_set_order
ts_bspline_dimension = _tinysplinepython.ts_bspline_dimension
ts_bspline_set_dimension = _tinysplinepython.ts_bspline_set_dimension
ts_bspline_len_control_points = _tinysplinepython.ts_bspline_len_control_points
ts_bspline_num_control_points = _tinysplinepython.ts_bspline_num_control_points
ts_bspline_sof_control_points = _tinysplinepython.ts_bspline_sof_control_points
ts_bspline_control_points = _tinysplinepython.ts_bspline_control_points
ts_bspline_control_point_at = _tinysplinepython.ts_bspline_control_point_at
ts_bspline_set_control_points = _tinysplinepython.ts_bspline_set_control_points
ts_bspline_set_control_point_at = _tinysplinepython.ts_bspline_set_control_point_at
ts_bspline_num_knots = _tinysplinepython.ts_bspline_num_knots
ts_bspline_sof_knots = _tinysplinepython.ts_bspline_sof_knots
ts_bspline_knots = _tinysplinepython.ts_bspline_knots
ts_bspline_set_knots = _tinysplinepython.ts_bspline_set_knots
ts_deboornet_knot = _tinysplinepython.ts_deboornet_knot
ts_deboornet_index = _tinysplinepython.ts_deboornet_index
ts_deboornet_multiplicity = _tinysplinepython.ts_deboornet_multiplicity
ts_deboornet_num_insertions = _tinysplinepython.ts_deboornet_num_insertions
ts_deboornet_dimension = _tinysplinepython.ts_deboornet_dimension
ts_deboornet_len_points = _tinysplinepython.ts_deboornet_len_points
ts_deboornet_num_points = _tinysplinepython.ts_deboornet_num_points
ts_deboornet_sof_points = _tinysplinepython.ts_deboornet_sof_points
ts_deboornet_points = _tinysplinepython.ts_deboornet_points
ts_deboornet_len_result = _tinysplinepython.ts_deboornet_len_result
ts_deboornet_num_result = _tinysplinepython.ts_deboornet_num_result
ts_deboornet_sof_result = _tinysplinepython.ts_deboornet_sof_result
ts_deboornet_result = _tinysplinepython.ts_deboornet_result
ts_bspline_init = _tinysplinepython.ts_bspline_init
ts_bspline_new = _tinysplinepython.ts_bspline_new
ts_bspline_copy = _tinysplinepython.ts_bspline_copy
ts_bspline_move = _tinysplinepython.ts_bspline_move
ts_bspline_free = _tinysplinepython.ts_bspline_free
ts_deboornet_init = _tinysplinepython.ts_deboornet_init
ts_deboornet_copy = _tinysplinepython.ts_deboornet_copy
ts_deboornet_move = _tinysplinepython.ts_deboornet_move
ts_deboornet_free = _tinysplinepython.ts_deboornet_free
ts_bspline_interpolate_cubic = _tinysplinepython.ts_bspline_interpolate_cubic
ts_bspline_eval = _tinysplinepython.ts_bspline_eval
ts_bspline_domain = _tinysplinepython.ts_bspline_domain
ts_bspline_is_closed = _tinysplinepython.ts_bspline_is_closed
ts_bspline_derive = _tinysplinepython.ts_bspline_derive
ts_bspline_insert_knot = _tinysplinepython.ts_bspline_insert_knot
ts_bspline_split = _tinysplinepython.ts_bspline_split
ts_bspline_buckle = _tinysplinepython.ts_bspline_buckle
ts_bspline_to_beziers = _tinysplinepython.ts_bspline_to_beziers
ts_bspline_to_json = _tinysplinepython.ts_bspline_to_json
ts_bspline_from_json = _tinysplinepython.ts_bspline_from_json
ts_bspline_save_json = _tinysplinepython.ts_bspline_save_json
ts_bspline_load_json = _tinysplinepython.ts_bspline_load_json
ts_knots_equal = _tinysplinepython.ts_knots_equal
ts_arr_fill = _tinysplinepython.ts_arr_fill
ts_distance = _tinysplinepython.ts_distance
class DeBoorNet(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, other: 'DeBoorNet'):
        _tinysplinepython.DeBoorNet_swiginit(self, _tinysplinepython.new_DeBoorNet(other))
    __swig_destroy__ = _tinysplinepython.delete_DeBoorNet
    knot = property(_tinysplinepython.DeBoorNet_knot_get)
    index = property(_tinysplinepython.DeBoorNet_index_get)
    multiplicity = property(_tinysplinepython.DeBoorNet_multiplicity_get)
    num_insertions = property(_tinysplinepython.DeBoorNet_num_insertions_get)
    dimension = property(_tinysplinepython.DeBoorNet_dimension_get)
    points = property(_tinysplinepython.DeBoorNet_points_get)
    result = property(_tinysplinepython.DeBoorNet_result_get)

# Register DeBoorNet in _tinysplinepython:
_tinysplinepython.DeBoorNet_swigregister(DeBoorNet)

class Domain(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _tinysplinepython.Domain_swiginit(self, _tinysplinepython.new_Domain(*args))
    min = property(_tinysplinepython.Domain_min_get)
    max = property(_tinysplinepython.Domain_max_get)
    __swig_destroy__ = _tinysplinepython.delete_Domain

# Register Domain in _tinysplinepython:
_tinysplinepython.Domain_swigregister(Domain)

class BSpline(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _tinysplinepython.BSpline_swiginit(self, _tinysplinepython.new_BSpline(*args))
    __swig_destroy__ = _tinysplinepython.delete_BSpline
    __call__ = _swig_new_instance_method(_tinysplinepython.BSpline___call__)
    control_point_at = _swig_new_instance_method(_tinysplinepython.BSpline_control_point_at)
    eval = _swig_new_instance_method(_tinysplinepython.BSpline_eval)
    is_closed = _swig_new_instance_method(_tinysplinepython.BSpline_is_closed)
    to_json = _swig_new_instance_method(_tinysplinepython.BSpline_to_json)
    from_json = _swig_new_instance_method(_tinysplinepython.BSpline_from_json)
    save = _swig_new_instance_method(_tinysplinepython.BSpline_save)
    load = _swig_new_instance_method(_tinysplinepython.BSpline_load)
    set_control_point_at = _swig_new_instance_method(_tinysplinepython.BSpline_set_control_point_at)
    insert_knot = _swig_new_instance_method(_tinysplinepython.BSpline_insert_knot)
    split = _swig_new_instance_method(_tinysplinepython.BSpline_split)
    buckle = _swig_new_instance_method(_tinysplinepython.BSpline_buckle)
    to_beziers = _swig_new_instance_method(_tinysplinepython.BSpline_to_beziers)
    derive = _swig_new_instance_method(_tinysplinepython.BSpline_derive)
    degree = property(_tinysplinepython.BSpline_degree_get)
    order = property(_tinysplinepython.BSpline_order_get)
    dimension = property(_tinysplinepython.BSpline_dimension_get)
    domain = property(_tinysplinepython.BSpline_domain_get)
    control_points = property(_tinysplinepython.BSpline_control_points_get, _tinysplinepython.BSpline_control_points_set)
    knots = property(_tinysplinepython.BSpline_knots_get, _tinysplinepython.BSpline_knots_set)

# Register BSpline in _tinysplinepython:
_tinysplinepython.BSpline_swigregister(BSpline)

class Utils(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    interpolate_cubic = _swig_new_static_method(_tinysplinepython.Utils_interpolate_cubic)
    knots_equal = _swig_new_static_method(_tinysplinepython.Utils_knots_equal)
    __swig_destroy__ = _tinysplinepython.delete_Utils

# Register Utils in _tinysplinepython:
_tinysplinepython.Utils_swigregister(Utils)
Utils_interpolate_cubic = _tinysplinepython.Utils_interpolate_cubic
Utils_knots_equal = _tinysplinepython.Utils_knots_equal

class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _tinysplinepython.delete_SwigPyIterator
    value = _swig_new_instance_method(_tinysplinepython.SwigPyIterator_value)
    incr = _swig_new_instance_method(_tinysplinepython.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_tinysplinepython.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_tinysplinepython.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_tinysplinepython.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_tinysplinepython.SwigPyIterator_copy)
    next = _swig_new_instance_method(_tinysplinepython.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_tinysplinepython.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_tinysplinepython.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_tinysplinepython.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_tinysplinepython.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_tinysplinepython.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_tinysplinepython.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_tinysplinepython.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_tinysplinepython.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_tinysplinepython.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _tinysplinepython:
_tinysplinepython.SwigPyIterator_swigregister(SwigPyIterator)



