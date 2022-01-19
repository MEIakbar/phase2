from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen, urlretrieve, quote
from urllib.parse import urljoin
import pandas as pd
from tqdm import tqdm
import csv
import json


class get_dpr_mpr():

    def __init__(self, all_config_dict):
        for key in all_config_dict:
            setattr(self, key, all_config_dict[key])

    @staticmethod
    def parse_config(auth_dict):
        """
        input function: selecting parameters from input file
        parameter required :
        1. type [required]: the file type must be .json

        :return: dictionary
        """
        list_dict_config = []
        all_config_dict = {
            "url_aceh": auth_dict['dprd_tk1']['Aceh']['url'],
            "url_sumut": auth_dict['dprd_tk1']['Sumatra Utara']['url'],
            "url_sumbar": auth_dict['dprd_tk1']['Sumatra Barat']['url'],
            "url_riau1": auth_dict['dprd_tk1']['Riau']['url_1'],
            "url_riau2": auth_dict['dprd_tk1']['Riau']['url_2'],
            "url_riau3": auth_dict['dprd_tk1']['Riau']['url_3'],
            "url_riau4": auth_dict['dprd_tk1']['Riau']['url_4'],
            "url_riau5": auth_dict['dprd_tk1']['Riau']['url_5'],
            "url_riau6": auth_dict['dprd_tk1']['Riau']['url_6'],
            "url_riau7": auth_dict['dprd_tk1']['Riau']['url_7'],
            "url_riau8": auth_dict['dprd_tk1']['Riau']['url_8'],
            "url_kepri": auth_dict['dprd_tk1']['Kepulauan Riau']['url'],
            "url_jambi": auth_dict['dprd_tk1']['Jambi']['url'],
            "url_bengkulu": auth_dict['dprd_tk1']['Bengkulu']['url'],
            "url_sumsel1": auth_dict['dprd_tk1']['Sumatra Selatan']['url_1'],
            "url_sumsel2": auth_dict['dprd_tk1']['Sumatra Selatan']['url_2'],
            "url_sumsel3": auth_dict['dprd_tk1']['Sumatra Selatan']['url_3'],
            "url_sumsel4": auth_dict['dprd_tk1']['Sumatra Selatan']['url_4'],
            "url_sumsel5": auth_dict['dprd_tk1']['Sumatra Selatan']['url_5'],
            "url_sumsel6": auth_dict['dprd_tk1']['Sumatra Selatan']['url_6'],
            "url_sumsel7": auth_dict['dprd_tk1']['Sumatra Selatan']['url_7'],
            "url_sumsel8": auth_dict['dprd_tk1']['Sumatra Selatan']['url_8'],
            "url_sumsel9": auth_dict['dprd_tk1']['Sumatra Selatan']['url_9'],
            "url_babel": auth_dict['dprd_tk1']['Kepulauan Bangka Belitung']['url'],
            "url_lampung1": auth_dict['dprd_tk1']['Lampung']['url_1'],
            "url_lampung2": auth_dict['dprd_tk1']['Lampung']['url_2'],
            "url_lampung3": auth_dict['dprd_tk1']['Lampung']['url_3'],
            "url_lampung4": auth_dict['dprd_tk1']['Lampung']['url_4'],
            "url_lampung5": auth_dict['dprd_tk1']['Lampung']['url_5'],
            "url_lampung6": auth_dict['dprd_tk1']['Lampung']['url_6'],
            "url_lampung7": auth_dict['dprd_tk1']['Lampung']['url_7'],
            "url_lampung8": auth_dict['dprd_tk1']['Lampung']['url_8'],
            "url_sulut": auth_dict['dprd_tk1']['Sulawesi Utara']['url'],
            "url_gorontalo1": auth_dict['dprd_tk1']['Gorontalo']['url_1'],
            "url_gorontalo2": auth_dict['dprd_tk1']['Gorontalo']['url_2'],
            "url_gorontalo3": auth_dict['dprd_tk1']['Gorontalo']['url_3'],
            "url_gorontalo4": auth_dict['dprd_tk1']['Gorontalo']['url_4'],
            "url_gorontalo5": auth_dict['dprd_tk1']['Gorontalo']['url_5'],
            "url_gorontalo6": auth_dict['dprd_tk1']['Gorontalo']['url_6'],
            "url_gorontalo7": auth_dict['dprd_tk1']['Gorontalo']['url_7'],
            "url_gorontalo8": auth_dict['dprd_tk1']['Gorontalo']['url_8'],
            "url_sulteng": auth_dict['dprd_tk1']['Sulawesi Tengah']['url'],
            "url_sulbar1": auth_dict['dprd_tk1']['Sulawesi Barat']['url_1'],
            "url_sulbar2": auth_dict['dprd_tk1']['Sulawesi Barat']['url_2'],
            "url_sulbar3": auth_dict['dprd_tk1']['Sulawesi Barat']['url_3'],
            "url_sulbar4": auth_dict['dprd_tk1']['Sulawesi Barat']['url_4'],
            "url_sulbar5": auth_dict['dprd_tk1']['Sulawesi Barat']['url_5'],
            "url_sulbar6": auth_dict['dprd_tk1']['Sulawesi Barat']['url_6'],
            "url_sulbar7": auth_dict['dprd_tk1']['Sulawesi Barat']['url_7'],
            "url_sulbar8": auth_dict['dprd_tk1']['Sulawesi Barat']['url_8'],
            "url_sulsel": auth_dict['dprd_tk1']['Sulawesi Selatan']['url'],
            "url_sultengga": auth_dict['dprd_tk1']['Sulawesi Tenggara']['url'],
            "url_papuabarat": auth_dict['dprd_tk1']['Papua Barat']['url'],
            "url_papua": auth_dict['dprd_tk1']['Papua']['url'],
            "url_bali": auth_dict['dprd_tk1']['Bali']['url'],
            "url_ntb": auth_dict['dprd_tk1']['Nusa Tenggara Barat']['url'],
            "url_ntt": auth_dict['dprd_tk1']['Nusa Tenggara Timur']['url'],
            "url_malukuutara": auth_dict['dprd_tk1']['Maluku Utara']['url'],
            "url_maluku": auth_dict['dprd_tk1']['Maluku']['url'],
            "url_kalbar": auth_dict['dprd_tk1']['Kalimantan Barat']['url'],
            "url_kalteng1": auth_dict['dprd_tk1']['Kalimantan Tengah']['url_1'],
            "url_kalteng2": auth_dict['dprd_tk1']['Kalimantan Tengah']['url_2'],
            "url_kalteng3": auth_dict['dprd_tk1']['Kalimantan Tengah']['url_3'],
            "url_kalteng4": auth_dict['dprd_tk1']['Kalimantan Tengah']['url_4'],
            "url_kalteng5": auth_dict['dprd_tk1']['Kalimantan Tengah']['url_5'],
            "url_kalsel1": auth_dict['dprd_tk1']['Kalimantan Selatan']['url_1'],
            "url_kalsel2": auth_dict['dprd_tk1']['Kalimantan Selatan']['url_2'],
            "url_kalsel3": auth_dict['dprd_tk1']['Kalimantan Selatan']['url_3'],
            "url_kalsel4": auth_dict['dprd_tk1']['Kalimantan Selatan']['url_4'],
            "url_kalsel5": auth_dict['dprd_tk1']['Kalimantan Selatan']['url_5'],
            "url_kaltim": auth_dict['dprd_tk1']['Kalimantan Timur']['url'],
            "url_kalut": auth_dict['dprd_tk1']['Kalimantan Utara']['url'],
            "url_jakarta1": auth_dict['dprd_tk1']['Daerah Khusus Ibukota Jakarta']['url_1'],
            "url_jakarta2": auth_dict['dprd_tk1']['Daerah Khusus Ibukota Jakarta']['url_2'],
            "url_jakarta3": auth_dict['dprd_tk1']['Daerah Khusus Ibukota Jakarta']['url_3'],
            "url_jakarta4": auth_dict['dprd_tk1']['Daerah Khusus Ibukota Jakarta']['url_4'],
            "url_jakarta5": auth_dict['dprd_tk1']['Daerah Khusus Ibukota Jakarta']['url_5'],
            "url_jakarta6": auth_dict['dprd_tk1']['Daerah Khusus Ibukota Jakarta']['url_6'],
            "url_jakarta7": auth_dict['dprd_tk1']['Daerah Khusus Ibukota Jakarta']['url_7'],
            "url_jakarta8": auth_dict['dprd_tk1']['Daerah Khusus Ibukota Jakarta']['url_8'],
            "url_jakarta9": auth_dict['dprd_tk1']['Daerah Khusus Ibukota Jakarta']['url_9'],
            "url_banten": auth_dict['dprd_tk1']['Banten']['url'],
            "url_jabar": auth_dict['dprd_tk1']['Jawa Barat']['url'],
            "url_jateng1": auth_dict['dprd_tk1']['Jawa Tengah']['url_1'],
            "url_jateng2": auth_dict['dprd_tk1']['Jawa Tengah']['url_2'],
            "url_jateng3": auth_dict['dprd_tk1']['Jawa Tengah']['url_3'],
            "url_jateng4": auth_dict['dprd_tk1']['Jawa Tengah']['url_4'],
            "url_jateng5": auth_dict['dprd_tk1']['Jawa Tengah']['url_5'],
            "url_jateng6": auth_dict['dprd_tk1']['Jawa Tengah']['url_6'],
            "url_jateng7": auth_dict['dprd_tk1']['Jawa Tengah']['url_7'],
            "url_jateng8": auth_dict['dprd_tk1']['Jawa Tengah']['url_8'],
            "url_yogya": auth_dict['dprd_tk1']['Daerah Istimewa Yogyakarta']['url'],
            "url_jatim": auth_dict['dprd_tk1']['Jawa Timur']['url']
        }
        list_dict_config.append(all_config_dict)
        return list_dict_config


    @staticmethod
    def load_config(json_path):
        """
        load Config from JSON file
        """
        f = open(json_path)
        json_config = json.load(f)

        return json_config


    @classmethod
    def load_config_json(cls, json_path):
        auth_json = cls.load_config(json_path)

        return cls(*cls.parse_config(auth_json))


    def get_data(self, url):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
        }
        r = requests.get(url, headers=headers)  # Using the custom headers we defined above
        soup = BeautifulSoup(r.content, 'html5lib') 
        return soup


    def get_aceh(self):
        try:
            nama_aceh = []
            soup = self.get_data(url)
            spans = soup.find_all('h3', {"style":"margin:0px!important"})
            for span in spans:
                nama_aceh.append(span.string)
            df = pd.DataFrame.from_dict({"nama":nama_aceh})
            if df.shape[0] > 5:
                print("get_aceh success..")
                return df
            else:
                print("get_aceh failed..")    
        except:
            print("get_aceh failed..")


    def get_sumut(self):
        try:
            df = pd.read_html(url)[10]
            if df.shape[0] > 5:
                print("get_sumut success..")
                return df
            else:
                print("get_sumut failed..")    
        except:
            print("get_sumut failed..")


    def get_sumbar(self, url):
        try:
            nama_sumbar = []
            soup = self.get_data(url)
            extensionsToCheck = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            divTag = soup.find_all("div", {"align" : "justify"})
            spans = divTag[0].find_all("div")
            for span in spans[10:]:
                if any(ext in span.string for ext in extensionsToCheck):
                    nama_sumbar.append(span.string)

            nama_sumbar = [e[2:] for e in nama_sumbar]
            df = pd.DataFrame({"Nama" : nama_sumbar})
            df["Deskripsi"] = "No Data"
            if df.shape[0] > 5:
                print("get_sumut success..")
                return df
            else:
                print("get_sumut failed..")    
        except:
            print("get_sumut failed..")


    def get_sumbar(self, url):
        try:


            if df.shape[0] > 5:
                print("get_sumut success..")
                return df
            else:
                print("get_sumut failed..")    
        except:
            print("get_sumut failed..")

    def get_dpr_data(self):
        df_mpr = self.get_mpr(self.url, self.Base_url)
        df_mpr.to_csv("./scrapping/result/dprd_tk1/mpr.csv", index=False)

        df_dpr = self.get_dpr(self.url, self.Base_url)
        df_dpr.to_csv("./scrapping/result/dpr_mpr/dpr.csv", index=False)


