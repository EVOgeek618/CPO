import json
def to_json(func):
    def warp(*args,**kwargs):
        return json.dumps(func(*args,**kwargs))
    return warp
@to_json
def dic(a,b):
    return None
print(dic(2,3))
