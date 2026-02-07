from zope.interface import Interface, implementer

class IGreeting(Interface):
    def greet(name):
        """Return a greeting string."""

@implementer(IGreeting)
class Greeter:
    def greet(self, name):
        return f"Hello, {name}! (from zope.interface)"