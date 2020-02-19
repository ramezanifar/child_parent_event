from child import Child
from event_handler import EventHandler
import time

class Parent:

    def __init__(self):
        self.my_child = Child()  # Create the object
        self.i = 0
        EventHandler.add_event_listener("Test", self.event_callback) # registers to an event and defines a callback function to process the event


    def event_callback(self,event_name,event_data):
        # This method is to process an event
        print event_data

    def call_child(self):
        # Send some data to the child
        data = "Message {} to child".format(str(self.i))
        self.i += 1
        self.my_child.parent_called(data)


if __name__ == '__main__':

    my_parent = Parent()
    try:
        while (True):
            my_parent.call_child()
            time.sleep(1)
    except KeyboardInterrupt:
        print "Ctrl+c detected. Program terminates"


