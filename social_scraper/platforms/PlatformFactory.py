from .PlatformEnumeration import PlatformEnumeration
from .Twitter import Twitter
from .PlatformNotFoundException import PlatformNotFoundException


class PlatformFactory:
    @staticmethod
    def create(platformEnumeration):
        platform = None

        if platformEnumeration == PlatformEnumeration.TWITTER:
            platform = Twitter()

        if platform == None:
            raise PlatformNotFoundException(
                "Platform \"{}\" does not exist".format(platformEnumeration))

        return platform
