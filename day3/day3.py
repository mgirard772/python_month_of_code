def unpack(d1):
    d3 = {}
    for k,v in d1.items():
        if not isinstance(v, (dict, list)):
            d3.update({k:v})
        else:
            if len(v) == 0:
                d3.update({k:None})
            elif isinstance(v, list):
                d3.update(unpack({k+"."+str(i):v[i] for i in range(len(v))}))
            else:
                d3.update(unpack({k+"."+nested_k:nested_v for nested_k, nested_v in v.items()}))
    return(d3)

if __name__ == "__main__":
    d2 = {"name": "Pac Man",
          "nickname": "Mr Puck",
          "activity": {
              'day': 'sleep',
              'night': {'eat': "pellets",
                        'fight': "monsters"}
          },
          "hobby": {},
          "madness": [1, ['a', {"name": 1, "gender": 2}, ['x', 'z']], 3]
          }
    print(unpack(d2))

