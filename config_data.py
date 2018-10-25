#configure the data to start with 
collection= gte_initial_state()
state_var = None
for datum in data_set:
    if condition(state_var):
        state_var = calculate_from(datum)
        new = modify(datum, state_var)
        collection.add_to(new)
    else:
        new = modify_differently(datum)
        collection.add_to(new)
#Now actually work with the data
for thing in collection:
    process(thing)



#----

def make_collection(data_set):
    collection = gte_initial_state();
    state_var = None
    for datum in data_set:
        state_var = calculate_from(datum, state_var)
        new = modify(datum, state_var)

        collection.add_to(new)

    else:
        new = modify_differently(datum)
        collection.add_to(new)

return collection

#Now acutally work with the data
for thing in make_collection(data_set):
    process(thing)
