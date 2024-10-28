import puuid_data
import match_csv_data
import match_list_data
import os
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()
    api_key = str(os.environ.get("APIKEY"))
    print(api_key[:-10])
    # puuid_data.get_puuid_data(api_key)
    # match_list_data.get_match_list(api_key)
    match_csv_data.get_match_csv_data(api_key,api_num=49, sqaure=10)

