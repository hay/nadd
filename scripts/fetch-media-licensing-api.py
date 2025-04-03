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

    req = requests.get(endpoint, params = params)
    data = req.json()

    return data

    # Parse the information and return in a more friendly format
    info = data["query"]["pages"][0]["imageinfo"][0]
    meta = info["extmetadata"]

    return {
        "url" : info["descriptionshorturl"],
        "description" : meta["ImageDescription"]["value"],
        "artist" : meta["Artist"]["value"],
        "license" : meta["LicenseShortName"]["value"],
        "license_url" : meta["LicenseUrl"]["value"]
    }

info = get_license_information("File:Erwin_Olaf.jpg", "nl")
print(json.dumps(info, indent = 4))
