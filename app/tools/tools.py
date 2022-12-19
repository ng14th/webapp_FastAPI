from typing import Dict
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