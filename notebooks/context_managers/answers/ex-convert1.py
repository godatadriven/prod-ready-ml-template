# We still need a Door object with a status:

class Door():
    def __init__(self, status = "The door is closed."):
        self.status = status

# Write the context manager:

import contextlib   

my_door = Door('The door is closed.')

@contextlib.contextmanager
def door_session(item='umbrella'):
    intial_doorstatus = my_door.status
        
    print('--- CREAK! ---')
    my_door.status='The door is open.'
        
    yield 

    print('--- CREAK! ---')
    my_door.status=intial_doorstatus
    

# Now test the context manager:

my_door = Door()

print(my_door.status)

with door_session() as ft:
    print(my_door.status)
    print("I now fetch my umbrella")
    
print(my_door.status)