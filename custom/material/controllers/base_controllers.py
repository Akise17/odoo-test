from werkzeug.wrappers import Response
import json

def mapper(message, data=None, status=200, object_only=False):
  res = { 
    "meta": {
      "status": status,
      "message": message,
    },
    "data": data
  }
  if object_only == True:
    return res

  response = Response(json.dumps(res), status=status, content_type='application/json')
  return response