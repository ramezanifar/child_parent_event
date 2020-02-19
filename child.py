from event_handler import EventHandler


class Child:

    def __init__(self):
        pass

    def parent_called(self,data):
        print data  # Message sent from parent
        out = "Message was received"
        EventHandler.dispatch_event("Test",out)






