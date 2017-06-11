from mygrations.core.parse.parser import parser

class index_key( parser ):

    # KEY account_id (account_id,name)
    rules = [
        { 'type': 'literal', 'value': 'KEY' },
        { 'type': 'regexp', 'name': 'key_name', 'value': '[^\(\s\)]+' },
        { 'type': 'literal', 'value': '(' },
        { 'type': 'delimited', 'name': 'fields', 'separator': ',', 'quote': '`' },
        { 'type': 'literal', 'value': ')' },
        { 'type': 'literal', 'value': ',', 'optional': True, 'name': 'ending_comma' }
    ]
