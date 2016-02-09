## Notes on blog implementation

### Sessions

The use of sessions demonstrates the use of a persistent store. Individual requests do not have a common state: only the persistent store can be used for this.

We can use MongoDB by providing a subclass of "Store", the class in the session module. The MongoDB store-subclass must provide an implentation for the interface as described in the Store class.
