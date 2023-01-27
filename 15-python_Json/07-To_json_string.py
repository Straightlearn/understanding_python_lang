#!/usr/bin/python3
''' function that returns the JSON representation of an object (string)
'''

import json


def to_json_string(my_obj):
    ''' module to_json_strin
     returns JSON representation
    '''
    return json.dumps(my_obj,indent=4)

obj={
    'name':'straightlearn',

    'sex':'Male',

    'complexion':'fair', 

    'Education':'undergraduate',

    'professional course':'surveying and geoinformatics',

    'other courses':'software engineering,graphics designing, etc',

    'height':'average',

    }

print('owner of these repo')
print(to_json_string(obj))
print('\nprogram ended')
