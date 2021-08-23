import requests
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USER_NAME = "YOUR_USER_NAME"
TOKEN = "YOUR_TOKEN"
GRAPH_ID = "YOUR_GRAPH_ID"

USER_PARAMS = {
    "token": TOKEN ,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}


# response = requests.post(url=PIXELA_ENDPOINT, json=USER_PARAMS)
# print(response.text)

graph_endpoint = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "hour",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
#check in browser: https://pixe.la/v1/users/heisenbug/graphs/graph01.html

#post a pixel today
# formatted_today = datetime.now().strftime("%Y%m%d")
# print(formatted_today)

# post_config = {
#     "date": formatted_today,
#     "quantity": "2"
# }
post_pixel_url = f"{graph_endpoint}/{GRAPH_ID}"
# response = requests.post(url=post_pixel_url, headers=headers, json=post_config)
# print(response.text)
def generate_date(year, month, day):
    return datetime(year=year, month=month, day=day).strftime("%Y%m%d")


def edit_quantity(date, quantity):
    return {
        "date": date,
        "quantity": str(quantity)


    }
# date = generate_date(2021, 8, 1)
# post_config = edit_quantity(date, 10)
# response = requests.post(url=post_pixel_url, headers=headers, json=post_config)
# print(response.text)

# use put() to edit the pixel
date = generate_date(2021, 8, 1)


put_pixel_url = f"{post_pixel_url}/{date}"
put_config = edit_quantity(date, 3)
# response = requests.put(url=put_pixel_url, headers=headers, json=put_config)
# print(response.text)


#use delete to delete the pixel or update it to quantity=0
delete_url = f"{post_pixel_url}/{date}"
# response = requests.delete(url=delete_url, headers=headers)
# print(response.text)
#change date