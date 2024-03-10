import configparser

class Config:
    def __init__(self):
        self.api_config = configparser.ConfigParser()
        self.api_config.read('whatsapp_chat.ini')

    def get_keys(self):
        return self.api_config

    
cfg = Config()
# apiconfig = cfg.get_keys()
# print(apiconfig['API_KEYS']['ACCOUNT_ID'])
# print(apiconfig['API_KEYS']['AUTH_TOKEN'])
