# Fetch metadata of a Commons image using the Mediawiki Action API and
# return a dict with the relevant information
import json
import requests

def get_license_information(filename:str, language:str= "en") -> dict:
    endpoint = "https://commons.wikimedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "formatversion": "2",
        "prop": "imageinfo",
        "titles": filename,
        "iiprop": "url|extmetadata",
        "iiextmetadatafilter": "|".join([
            "ImageDescription",
            "Artist",
            "LicenseShortName",
            "LicenseUrl"
        ]),
        "iiextmetadatalanguage": language,
        "uselang": language,
    }

    req = requests.get(
        endpoint,
        params = params,
        # Note that a user-agent is required
        headers = {
            "User-Agent" : "MyTool/0.1 (https://example.com;admin@example.com)"
        }
    )
    data = req.json()

    return data

info = get_license_information("File:Erwin_Olaf.jpg", "nl")
print(json.dumps(info, indent = 4))