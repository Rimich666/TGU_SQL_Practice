class ValueType(object):
    text = 'string',
    integer = 'integer',
    real = 'float',
    date = 'datetime',
    bool = 'boolean'
    map = {
        'INTEGER': integer,
        'Datetime': date,
        'Utf8': text,
        'utf8': text,
        'Int64': integer,
        'Int32': integer,
        'Bool': bool
    }
