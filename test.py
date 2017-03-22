from __future__ import absolute_import

from pprint import pprint

from appannie import AppAnnie

api_key = 'a966b8cd82dad952c23e359b933e0ba4671f31c4'
api = AppAnnie(api_key)

#pprint(api.aso.keywords_performance('ios', 922103212, 'mcdonalds', '2017-02-13', '2017-03-13', 'US', 'iphone'))
#pprint(api.store('ios').app(922103212).details())
#pprint(api.store('ios').ranking('US', 'Overall > Books'))

#pprint(api.meta().markets())
pprint(
        api.intelligence('all-android').user_retention(922103212, 'US')
)

# 382823
# 922103212
# break_down='date'
# start_date='2017-02-13', end_date='2017-03-13'


# ```python
# >> api.metadata().countries()
# [{u'country_code': u'AD', u'country_name': u'Andorra'},
#  {u'country_code': u'AE', u'country_name': u'United Arab Emirates'},
#  ...
# ]

# >> api.metadata().currencies()
# [{u'currency_code': u'AUD',
#   u'full_name': u'Australian dollar',
#   u'symbol': u'A$'},
#  {u'currency_code': u'BGN',
#   u'full_name': u'Bulgarian lev',
#   u'symbol': u'\u043b\u0432'},
#   ...
# ]


# >> api.metadata().markets()
# [{u'markets': [{u'market_code': u'ios', u'market_name': u'iOS Store'},
#                {u'market_code': u'mac', u'market_name': u'Mac Store'},
#                {u'market_code': u'google-play',
#                 u'market_name': u'Google Play'},
#                ...
#               ],
#   u'vertical_code': u'apps',
#   u'vertical_name': u'Apps'},
#  {u'markets': [{u'market_code': u'aarki', u'market_name': u'Aarki'},
#                {u'market_code': u'adbuddiz', u'market_name': u'Adbuddiz'},
#                {u'market_code': u'adcolony', u'market_name': u'AdColony'},
#                {u'market_code': u'admob', u'market_name': u'AdMob'},
#                ...
#               ],
#   u'vertical_code': u'ads',
#   u'vertical_name': u'Ads'}
# ]


# >> api.metadata().apps('ios').categories()
# {u'Overall': u'Overall',
#  u'Overall > Books': u'Books',
#  u'Overall > Education': u'Education',
#  u'Overall > Entertainment': u'Entertainment',
#  u'Overall > Finance': u'Finance',
#  u'Overall > Kids > 5 & Under': u'5 & Under',
#  ...
# }


# >> api.metadata().apps('ios').devices()
# [{u'device_code': u'iphone', u'device_name': u'iPhone'},
#  {u'device_code': u'ipad', u'device_name': u'iPad'}]

# >> api.metadata().apps('ios').feeds()
# [{u'feed_code': u'free', u'feed_name': u'Free'},
#  {u'feed_code': u'paid', u'feed_name': u'Paid'},
#  {u'feed_code': u'grossing', u'feed_name': u'Grossing'}]

# >> api.metadata().apps('google-play').package_code_to_id(['com.appannie.app', 'com.android.chrome'])
# [{u'package_code': u'com.android.chrome', u'product_id': 206000000234348}.
#  {u'package_code': 'com.appannie.app', u'product_id': 206707896576949}]
# ```

# ## Store Top Charts

# ```python
# >> api.store('ios').ranking('US', 'Overall > Games')
# [{country: "US",
#   category: "Overall > Games",
#   feed: "free",
#   date: "2013-08-24",
#   rank: 1,
#   rank_variation: 1,
#   product_id: 123456,
#   product_name: "Demo App Name",
#   icon: "http://www.appannie.com/pics/12.png",
#   price: 1,
#   has_iap: True,
#   publisher_name: "Demo Publisher Name",
#   publisher_id: 123456
#  },
#  ...
# ]
# ```
