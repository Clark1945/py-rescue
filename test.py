import json
a='{"JSON":"JSON"}'
try:
    input_data = json.loads(a)
    output_data = json.dumps(input_data, indent=4)
except ValueError as e:
    print("invalid json passed")
print(a)