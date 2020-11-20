from .PlatformEnumeration import PlatformEnumeration
from .PlatformNotFoundException import PlatformNotFoundException
from .Twitter import Twitter
from .Instagram import Instagram

class PlatformFactory:
    @staticmethod
    def create(platformEnumeration):
        platform = None

        if platformEnumeration == PlatformEnumeration.TWITTER:
            platform = Twitter()
        elif platformEnumeration == PlatformEnumeration.INSTAGRAM:
            platform = Instagram()

        if platform == None:
            raise PlatformNotFoundException(
                "Platform \"{}\" does not exist".format(platformEnumeration))

        return platform
