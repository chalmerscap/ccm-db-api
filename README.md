# CCM database utils
## Installation
#### pip
```pip install git```  
```pip install git+https://github.com/maxijohansson/borsdata_api_utils.git```
#### conda
```conda install pip```	(probably unnecessary)

If using a conda environment, navigate to the environment's `Scripts` dir (with cd). the `envs` dir is located in the main conda dir.

```...\envs\env_name\Scripts\>```

Install the git package and this package.

```pip install git```  
```pip install git+https://github.com/maxijohansson/ccm-db-api.git```

#### updating
Add  `--upgrade` flag:

```pip install --upgrade git+https://github.com/maxijohansson/ccm-db-api.git```

## Usage

```import ccm_db_api as db```

There are two available classes:

```borsdata_db = db.Borsdata_db(key)```

The `Borsdata_db` class contains functions for retrieving data from Börsdata's database. This requires an api key.

```ccm_db = db.CCM_db(password)```

The `CCM_db` class contains functions for retrieving data from CCM's database. This requires a password.
___
The functions in both classes generally return pandas dataframes, so for example, ```df = borsdata_db.instruments()``` will provide a dataframe of all available instruments.


