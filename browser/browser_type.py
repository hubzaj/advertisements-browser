from enum import Enum, auto


class BrowserType(Enum):
    CHROME = auto()

    @classmethod
    def get_browser(cls, name: str) -> 'BrowserType':
        try:
            return cls[name.upper()]
        except KeyError:
            raise KeyError(f"[{name}] browser isn't supported - choose one of {list(map(str, cls))}")
