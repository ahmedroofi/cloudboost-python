# cloudboost-python


## Initialize
```
from cloudboost.CB import CB
cb = CB(url, app_id, key)
```

## Save item
```
cb.data.save(tablename, object)
return the object saved on db.
eg. cb.data.save("todo", {"task": "Haircut"})
```

## Find Item
```
cb.data.find(tablename, queryObject)
eg. cb.data.find("todo", {"task": "bookFlight"})
return the list of objects, matched query.
```

## Delete item
```
obj_to_delete = cb.data.find(tablename, queryObject)
cb.data.delete(tablename, obj_to_delete.json()[0])
return empty list
```

## Count Items
```
cb.data.count(tablename, queryObject)
eg. cb.data.count("todo", {"task": "Haircut"})
return count of objects, which matched query
```

## User signup
```
cb.user.signup_user(username, email, password)
```
