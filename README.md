# pytradier

pytradier is a forked version of tradier-python (0.1.4), that is no longer maintained by its owner. It is a python client for interacting with the Tradier API.


## Getting Started

You will need a Tradier account token which you can download from your account after logging in. 

The client also takes an optional default_account_id which can make it easier to get information if you only have one account. 

The default endpoint is the sandbox. You will need to set the endpoint to the brokerage endpoint for live use. 

Reference documentation for the API can be found here:

https://documentation.tradier.com/brokerage-api/overview/market-data


### Installing

pip install pytradier

### Exemple

```
import os

from pytradier import TradierAPI

token = os.environ["TRADIER_TOKEN_SANDBOX"]
account_id = os.environ["TRADIER_ACCOUNT_ID1"]
t = TradierAPI(token=token, default_account_id=account_id)

profile = t.get_profile()
print(profile)
```


## Version History

* 0.1.0
    * Initial release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

