from typing import *
import ujson

def _dumps_dict_for_hash_map(data: Dict) -> Dict:
        formatted = {}
        for k, v in data.items():
            if isinstance(v, (list, tuple, dict, bool)) or v in (None, ):
                try:
                    formatted[k] = ujson.dumps(v)
                except ValueError:
                    formatted[k] = v    
            else:
                formatted[k] = v
        return formatted
    
def convert_data_to_byte(data):
    if isinstance(data, (list, tuple, dict, bool)):
        try :
            data_json = ujson.dumps(data)
            result = data_json.encode()
            return result
        except Exception as e :
            print(f'Convert data to byte got exception {e}')
            return None
    else:
        try: 
            result = data.encode()
            return result
        except Exception as e :
            print(f'Convert data to byte got exception {e}')
            return None
        