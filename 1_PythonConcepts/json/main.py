# json is Javascript Object Notation
# here is an example for json
"""
{
  "name": "Lenin",
  "age": 30,
  "twitter": "@pylenin",
  "website": "www.100daysofdata.com"
}
"""
# it looks same as dictionary but
# Dictionary is a data type whereas JSON is a data format.


# writing json into a file we use json.dump()

# json serialization
import json

data = {
      "name": "Lenin Mishra",
  "age": 30,
  "hobby": ["Biking", "Blogging", "Cooking"],
  "websites": [
    {
    "url": "https://www.pylenin.com",
    "Total blogs": "88",
    "description": "Everything about Python"
    },
    {
    "url": "https://www.100daysofdata.com",
    "Total blogs": "3",
    "description": "Everything about Data"          
    }]
}

with open('details.json', 'w') as file:
    json.dump(data, file)

data_string_json = json.dumps(data)
print(data_string_json)
"""
output:
{"name": "Lenin Mishra", "age": 30, "hobby": ["Biking", "Blogging", "Cooking"], "websites": [{"url": "https://www.p
ylenin.com", "Total blogs": "88", "description": "Everything about Python"}, {"url": "https://www.100daysofdata.com
", "Total blogs": "3", "description": "Everything about Data"}]}
"""

# how to prittyfy this json data
data_string_json = json.dumps(data, indent=4)
print(data_string_json)

# how to sort the keys
data_string_json = json.dumps(data, indent=4, sort_keys=True)
print(data_string_json)

"""
difference between json dump() and dumps()
"""

"""
If you want to dump the JSON into a file, then you should use json.dump(). If you only need it as a string, then use json.dumps().
"""

# JSON deserialization

"""
    json.loads()
"""
data = '{"name": "Lenin", "website": "100daysofdata.com", "age":30}'

json_dict = json.loads(data)
print(type(json_dict))
print(json_dict)

"""
    json.load()
"""
file_name = "details.json"

with open(file_name, "r") as r:
    data = json.load(r)

print(type(data)) # type of dictionary

for key, values in data.items():
    print(key, values)

