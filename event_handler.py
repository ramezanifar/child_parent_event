
class EventHandler:
    ''' This class accept listeners to register some events. when the event is invoked by an initiator, this class
    calls informs the listener by invoking a callback function in the listener class and passing the data to it'''
    _events = dict()

    @classmethod
    def __del__(cls):
        """
        Remove all listener references at destruction time
        """
        cls._events = None

    @classmethod
    def has_listener(cls, event_name, listener):
        """
        Return true if listener is register to event_type
        """
        # Check for event type and for the listener
        if event_name in cls._events.keys():
            return listener in cls._events[event_name]
        else:
            return False

    @classmethod
    def dispatch_event(cls, event, data):
        """
        Dispatch an instance of Event class
        """
        # Dispatch the event to all the associated listeners
        if event in cls._events.keys():
            listeners = cls._events[event]
            for listener in listeners:
                listener(event, data)

    @classmethod
    def dispatch_event_with_reply(cls, event, data):
        """
        Dispatch an instance of Event class
        """
        # Dispatch the event to all the associated listeners and return their reply to the event initiator
        if event in cls._events.keys():
            listeners = cls._events[event]
            reply=[]  # the reply for each listener is appended here
            for listener in listeners:
                this_reply=listener(event,data)
                reply.append(this_reply)
        return reply # Return the response of the listener to the caller

    @classmethod
    def add_event_listener(cls, event_name, listener):
        """
        Add an event listener for an event type
        """
        # Add listener to the event type
        if not cls.has_listener(event_name, listener):
            listeners = cls._events.get(event_name, [])

            listeners.append(listener)

            cls._events[event_name] = listeners






