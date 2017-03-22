# AppAnnie
Python library which can query data from the App Annie platform. Platform Partnership API is currently not supported.


# Creating the client:

```python
from appannie import AppAnnie


api = AppAnnie('my api key')

```

# Available calls:

## Metadata:

```python
api.meta().countries()
api.meta().currencies()
api.meta().verticals().get('ads')
api.meta().store().all()
api.meta().store('ios').categories()
api.meta().store('ios').devices()
api.meta().store('ios').feeds()
api.store('google-play').package_code_to_id([u'com.mcdonalds.app', u'us.com.mcdonalds.mcdordering'])
api.meta().features('ios').categories()
api.meta().features('ios').types()
```

## Store top charts:

```python
api.store('ios').ranking('US', 'Overall > Games')
```

## App calls:

```python
api.store('ios').app(922103212).details()
api.store('ios').app(922103212).ads(ad_item_type='campaign')  # ad_item_type is optional
api.store('ios').app(922103212).ratings()
api.store('ios').app(922103212).featured('2017-03-03', '2017-03-23')
api.store('ios').app(922103212).featured_history('2017-03-03', '2017-03-23')
api.store('ios').app(922103212).reviews('2017-03-03', '2017-03-23')
api.store('ios').app(922103212).ranks('2017-03-03', '2017-03-23')
```

## Keyword related calls:

```python
api.store('ios').keyword(922103212).explore('US', 'iphone', '2017-03-23', 'uber')
api.store('ios').keyword(922103212).ranked('US', 'iphone', '2017-03-23')
api.store('ios').keyword(922103212).performance('US', 'iphone', '2017-03-03', '2017-03-23',
					        ['uber', 'netflix'])
```


## Account calls:

```python
api.account().all()
api.account(382823).ads()
api.account(382823).sales()

```

## Account products calls:

```python
api.account(382823).product().all()  # the product list is paginated
api.account(382823).product(922103212).page(1)
api.account(382823).product(922103212).iaps()
api.account(382823).product(922103212).sales(union_key='sales_list')  # special parameter union_key
api.account(382823).product(922103212).usage('2017-03-03', '2017-03-23')
api.account(382823).product(922103212).metrics()
```

## Intelligence API calls:

```python
api.intelligence('ios').app_ranking('US', 'iphone', 'Overall > Books')
api.intelligence('ios').app_history(922103212, 'US', 'downloads')
api.intelligence('ios').publisher_ranking('US', 'iphone', 'Overall')
api.intelligence('ios').publisher_history('US', 'Overall', 368677371, 'revenue')
api.intelligence('ios').usage_ranking('US', 'iphone', 'Overall')
api.intelligence('ios').usage_history(922103212, 'US')
api.intelligence('all-android').user_retention(922103212, 'US')
api.intelligence('ios').cross_app_usage(922103212, 'US', 'Overall')
api.intelligence('ios').demographics(922103212, 'US')
```


# Conventions:

There is a simple convention using this library: required parameters are using positional arguments, while optional ones are using keyword arguments.

Some calls are paginated. You can get the result for a specific page or all results, depending on your needs:

```python
api.store('ios').app(922103212).ads().all()
api.store('ios').app(922103212).ads().page(1)
```

When getting a specific page result you will also get info relevant to pagination, like total page number and next & previous page URI. Some calls are using a special parameter (`union_key`) when getting the result. This is very call-specific and will be detailed to each call that use it.

When making calls you should check for ```appannie.exception.AppAnnieException```, which is the base class for all exceptions thrown by this client.

# Misc

Based on documentation from [AppAnnie Knowledge Base](https://support.appannie.com/hc/en-us/categories/202773667-API). API calls will be detailed in the [GitHub Wiki](https://github.com/webhue/appannie/wiki), where you can get a direct link to underlying documentation. This should be useful to get the list of optional parameters and other relevant details.

MIT License.
