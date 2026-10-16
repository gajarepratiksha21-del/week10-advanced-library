
class PluginMeta(type):
    """Register plugin classes automatically."""

    registry: dict[str, type] = {}

    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)

        if namespace.get("register_plugin", False):
            mcs.registry[name] = cls

        return cls


class Plugin(metaclass=PluginMeta):
    """Base class for all plugins."""

    register_plugin = False

    def run(self) -> str:
        raise NotImplementedError("Plugins must implement run()")


class GreetingPlugin(Plugin):
    """A simple greeting plugin."""

    register_plugin = True

    def run(self) -> str:
        return "Hello from the plugin!"


def get_plugins() -> dict[str, type]:
    """Return all registered plugins."""
    return PluginMeta.registry.copy()
