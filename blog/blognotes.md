## Notes on blog implementation

What kind of functionality do we offer? 

* multiple users; every user may have its own blog?
* multiple users - for comments;
* blog may have comments - anonymous? or only for users logged in?
* posts may be created; and may be edited afterwards.
** do we keep a history of edits?


### Sessions

The use of sessions demonstrates the use of a persistent store. Individual requests do not have a common state: only the persistent store can be used for this.

We can use MongoDB by providing a subclass of "Store", the class in the session module. The MongoDB store-subclass must provide an implentation for the interface as described in the Store class.

### API

* creation of a session: `mysession = web.session.Session(app, initializer)`
* end a session: `mysession.kill()`

(How to fill in the user name; how to get the user name?)

A session may have data; this data can be stored and retrieved by:

* `mysession.__getitem__(key)`
* `mysession.__setitem__(key, value)`

These functions correspond to the assignment and use of object-properties like in: `x.p = e` and `print(x.p)`.

* Note that these are defined for objects (class instances), but not for dictionaries. In JS, this is different.

### HTTP authorization

A disadvantage of this kind of authorization is that there is no well-defined "logout".

