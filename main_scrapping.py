import pandas
import os
import logging
import time
from scrapping.scrapping_kabinet import get_kabinet
from scrapping.scrapping_dpr_mpr import get_dpr_mpr

import warnings
warnings.filterwarnings("ignore")


if __name__ == "__main__":
    logging.info('Load Config... ')
    json_path = "./scrapping/config.json"
    scrp_kabinet = get_kabinet.load_config_json(json_path)
    scrp_dpr_mpr = get_dpr_mpr.load_config_json(json_path)

    scrp_kabinet.get_kabinet_data()
    scrp_dpr_mpr.get_dpr_data()
