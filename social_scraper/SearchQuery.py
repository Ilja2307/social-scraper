class SearchQuery:

    def __init__(self, query):
        self.query = query
        self.maximumItemCount = 0
        self.isVerbose = False

    def getQuery(self):
        query = self.query

        if self.startDate != None:
            query = f"{query} since:{self.startDate}"

        if self.endDate != None:
            query = f"{query} until:{self.endDate}"

        return query

    def setMaximumItemCount(self, maximumItemCount):
        self.maximumItemCount = maximumItemCount

    def setStartDate(self, startDate):
        self.startDate = startDate

    def setEndDate(self, endDate):
        self.endDate = endDate

    def getMaximumItemCount(self):
        return self.maximumItemCount

    def setVerboseEnabled(self, isVerbose):
        self.isVerbose = isVerbose

    def isVerboseEnabled(self):
        return self.isVerbose
