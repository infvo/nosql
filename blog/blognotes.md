## Notes on blog implementation

### Sessions

The use of sessions demonstrates the use of a persistent store. Individual requests do not have a common state: only the persistent store can be used for this.

We can use MongoDB by providing a subclass of "Store", the class in the session module. The MongoDB store-subclass must provide an implentation for the interface as described in the Store class.

### API

* creation of a session: `mysession = web.session.Session(app, initializer)`
* end a session: `mysession.kill()`

(How to fill in the user name; how to get the user name?)

A session may have data; this data can be stored and retrieved by:

* `mysession.__getitem(key)`
* `mysession.__setitem(key, value)`

### HTTP authorization

A disadvantage of this kind of authorization is that there is no well-defined "logout".

