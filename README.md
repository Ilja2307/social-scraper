# Wrapper for snscrape

## Installation

Open your command line and copy & paste the following:

`pip3 install git+https://github.com/leoyn/social-scraper.git`

---

Requirements:

-   Python 3.8+

---

## Example

```python
from social_scraper import PlatformFactory, SearchQuery, PlatformEnumeration
import datetime


# Configure search query
# Twitter supports the following operators: https://www.tweetarchivist.com/about/operators
query = SearchQuery("Sainsburys")

# Omit this when you want to get all tweets. This can take infinite time, so be careful
query.setMaximumItemCount(3000)

# This has no proper function other than providing feedback in console. can be omitted as well
query.setVerboseEnabled(True)

query.setStartDate(datetime.date(2015, 1, 15))
query.setEndDate(datetime.date(2015, 1, 16))


# Tweets will be saved in the "test.csv" file, open it with excel
PlatformFactory.create(PlatformEnumeration.TWITTER).search(
    query).saveAsCSV("test.csv")
```
