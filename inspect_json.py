import json
import inspect

source_code = inspect.getsource(json.dump)


print(source_code)
