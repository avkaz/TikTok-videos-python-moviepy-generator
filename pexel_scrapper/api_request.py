class ApiRequest:
    def __init__(self):
        self.url = "https://www.pexels.com/en-us/api/v3/search/videos"

    def get_headers(self):
        headers = {
            "authority": "www.pexels.com",
            "accept": "*/*",
            "accept-language": "cs-CZ,cs;q=0.9,en-US;q=0.8,en;q=0.7,ru-RU;q=0.6,ru;q=0.5",
            "authorization": "",
            "baggage": "sentry-environment=production,sentry-release=8fbd2a0b026db16b90d735fe2890a775d8ab130a,sentry-public_key=33ca4e93921442e3b9096c7950630125,sentry-trace_id=066e10182d614da49dfd0958c729720a,sentry-sample_rate=0.0005,sentry-transaction=GET%20%2Fapi%2Fv3%2Fsearch%2Fvideos%3Fpage%3D2%26per_page%3D24%26query%3Dwalking%26orientation%3Dall%26size%3Dall%26color%3Dall%26seo_tags%3Dtrue,sentry-sampled=false",
            "cookie": "_gid=GA1.2.1458087604.1703683448; country-code-v2=CZ; g_state={'i_p':1703691971685,'i_l':1}; cf_clearance=kmAqipkkzxgahAUP9GMa.OzoKLJz.9EjZjHMuOTdA4o-1703692782-0-2-2c9572b9.a99f5151.13602938-0.2.1703692782; _ga=GA1.2.641394981.1703683448; ab.storage.deviceId.5791d6db-4410-4ace-8814-12c903a548ba=%7B%22g%22%3A%22eb829a5b-d3c3-bdef-055e-947a1e342391%22%2C%22c%22%3A1703683448078%2C%22l%22%3A1703692875403%7D; ab.storage.sessionId.5791d6db-4410-4ace-8814-12c903a548ba=%7B%22g%22%3A%228a7c3f18-ddcc-4248-6b9b-d87880bcac6d%22%2C%22e%22%3A1703694723073%2C%22c%22%3A1703692875403%2C%22l%22%3A1703692923073%7D; OptanonAlertBoxClosed=2023-12-27T16:02:09.487Z; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Dec+27+2023+17%3A02%3A09+GMT%2B0100+(Central+European+Standard+Time)&version=202301.1.0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false; __cf_bm=Kv137Hp8GF5C5bal9K1lDv8CPiehIXtnD49HVba1AfI-1703701631-1-AZdED92c7rFJyxGhlbRAjby7OWhcQD0aqcZlBYkZWc04o75iXqlxrkjuXrBgnpwC9diqJELkiqTNwHgQv0dielk=; _gat=1; _sp_ses.9ec1=*; _sp_id.9ec1=df694b9c-122e-4142-8f41-d99bf47ea271.1703683448.3.1703701635.1703692923.051debf6-a159-4d3c-96da-ef1a2750995e.ddfee5f6-4609-4b29-8720-64d388f3fa6f.1497276e-933f-4128-9509-2d09cf56eb39.1703701634454.6; _gat_UA-50832266-1=1; _ga_8JE65Q40S6=GS1.1.1703701242.3.1.1703701635.0.0.0",
            "if-none-match": "W/'c40685b2323c989688c0b101640a1530'",
            "referer": "https://www.pexels.com/search/videos/walking/",
            "sec-ch-ua": "'Not_A Brand';v='8', 'Chromium';v='120', 'Google Chrome';v='120'",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "'macOS'",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "secret-key": "H2jk9uKnhRmL6WPwh89zBezWvr",
            "sentry-trace": "066e10182d614da49dfd0958c729720a-a80e66acb3d502a3-0",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "x-client-type": "react",
            "x-forwarded-cf-connecting-ip": "",
            "x-forwarded-cf-ipregioncode": "",
            "x-forwarded-http_cf_ipcountry": ""
        }
        return headers

    def get_querystring(self):
        querystring = {"page":"1","per_page":"300","query":"walking","orientation":"portrait","size":"all","color":"all","seo_tags":"true"}
        return querystring
