class SearchQuery:

    def __init__(self, query):
        self.query = query
        self.maximumItemCount = 0
        self.isVerbose = False
        self.startDate = None
        self.endDate = None

    def getQuery(self):
        return self.query

    def setMaximumItemCount(self, maximumItemCount):
        self.maximumItemCount = maximumItemCount

    def setStartDate(self, startDate):
        self.startDate = startDate

    def getStartDate(self):
        return self.startDate

    def setEndDate(self, endDate):
        self.endDate = endDate

    def getEndDate(self):
        return self.endDate

    def getMaximumItemCount(self):
        return self.maximumItemCount

    def setVerboseEnabled(self, isVerbose):
        self.isVerbose = isVerbose

    def isVerboseEnabled(self):
        return self.isVerbose
