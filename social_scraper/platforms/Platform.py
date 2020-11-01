import abc


class Platform:
    @abc.abstractmethod
    def search(self, searchQuery):
        raise NotImplementedError("Please Implement this method")
