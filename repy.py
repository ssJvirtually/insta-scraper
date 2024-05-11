import requests
import json


url = "https://www.instagram.com/api/graphql"

headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/x-www-form-urlencoded",
    "dpr": "2",
    "sec-ch-prefers-color-scheme": "light",
    "sec-ch-ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Google Chrome\";v=\"122\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"122.0.6261.113\", \"Not(A:Brand\";v=\"24.0.0.0\", \"Google Chrome\";v=\"122.0.6261.113\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-model": "\"Nexus 5\"",
    "sec-ch-ua-platform": "\"Android\"",
    "sec-ch-ua-platform-version": "\"6.0\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "viewport-width": "843",
    "x-asbd-id": "129477",
    "x-csrftoken": "8HmpOJqMiPtINoRMv9Qh3Z",
    "x-fb-friendly-name": "PolarisPostActionLoadPostQueryLegacyQuery",
    "x-fb-lsd": "AVpGd9Ej63k",
    "x-ig-app-id": "1217981644879628",
    "cookie": "csrftoken=8HmpOJqMiPtINoRMv9Qh3Z; dpr=2.0000000596046448; _js_ig_did=98FFB105-135B-4996-B474-EFFFC9B9DC58; _js_datr=z1zxZTCcvjYwZyhOnHxIwYU2; mid=ZfFc0QABAAGwlhcOg3EWkInT_JnV; ig_did=98FFB105-135B-4996-B474-EFFFC9B9DC58; ig_nrcb=1",
    "Referer": "https://www.instagram.com/p/C4DJ21bSer6/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
}

body = {
    "av": "0",
    "__d": "www",
    "__user": "0",
    "__a": "1",
    "__req": "3",
    "__hs": "19795.HYP%3Ainstagram_web_pkg.2.1..0.0",
    "dpr": "1",
    "__ccg": "UNKNOWN",
    "__rev": "1012021408",
    "__s": "733tif%3Aehboaz%3Awasi2u",
    "__hsi": "7345754512403786307",
    "__dyn": "7xeUjG1mxu1syUbFp40NonwgU29zEdF8aUco2qwJw5ux609vCwjE1xoswaq0yE7i0n24oaEd86a3a1YwBgao6C0Mo2iyovw8O4U2zxe2GewGwso88cobEaU2eUlwhEe87q7U1bobpEbUGdwtU662O0z8c86-3u2WE5B0bK1Iwqo5q1IQp1yUoxe4UrAwCAxW",
    "__csr": "gpnk8OyiHKDXQyWtKKAqjNaFvFFGcycC48-uayZllqytz9eaCgKiGy_Q8hUGax7gSiAWtae8HGV-EhzF9oFCAyUyFGGHy9d4yqVAUPyHDAU8GBypby44qyEkxl2olw05hiIK0beCDg12Ey0dYw1MG1dwjEj4VUeeE24w-hx8aQ04ko3BBkE7O6Esw1gW0hCyU02j-w",
    "__comet_req": "7",
    "lsd": "AVpGd9Ej63k",
    "jazoest": "2878",
    "__spin_r": "1012021408",
    "__spin_b": "trunk",
    "__spin_t": "1710316751",
    "fb_api_caller_class": "RelayModern",
    "fb_api_req_friendly_name": "PolarisPostActionLoadPostQueryLegacyQuery",
    "variables": "{\"shortcode\":\"C4DJ21bSer6\",\"fetch_comment_count\":40,\"fetch_related_profile_media_count\":3,\"parent_comment_count\":24,\"child_comment_count\":3,\"fetch_like_count\":10,\"fetch_tagged_user_count\":null,\"fetch_preview_comment_count\":2,\"has_threaded_comments\":true,\"hoisted_comment_id\":null,\"hoisted_reply_id\":null}",
    "server_timestamps": "true",
    "doc_id": "7341532402634560"
}

response = requests.post(url, headers=headers, data=body)

# Pretty print the JSON response
print(json.dumps(response.json(), indent=4))