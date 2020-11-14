# CCM database python api integration
## Installation
#### pip
```pip install git```  
```pip install git+https://github.com/maxijohansson/borsdata_api_utils.git```
#### conda
```conda install pip```	(probably unnecessary)

If using a conda environment, navigate to the environment's `Scripts` dir (with cd). The `envs` dir is located in the main conda dir.

```...\envs\env_name\Scripts\>```

Install the git package and this package.

```pip install git```  
```pip install git+https://github.com/maxijohansson/ccm-db-api.git```

#### updating
Add  `--upgrade` flag:

```pip install --upgrade git+https://github.com/maxijohansson/ccm-db-api.git```

## Usage

```import ccm_db_api as api_utils```

There are two available classes:

```borsdata = api_utils.Borsdata_db(key)```

The `Borsdata_db` class contains functions for retrieving data from Börsdata's database. This requires an api key.

```guldgruvan = api_utils.Guldgruvan(key)```

The `Guldgruvan` class contains functions for retrieving data from CCM's database. This requires an api key.  

The functions in both classes generally return pandas dataframes, so for example, ```df = borsdata.instruments()``` will provide a dataframe of all available instruments.

### Guldgruvan
#### Available functions:
* ```guldgruvan.instruments()```: Returns a dataframe with all available instruments
* ```guldgruvan.dailyprices(instrument, first, last)```: Returns a dataframe with daily price data for ```instrument``` between dates ```first``` and ```last```



