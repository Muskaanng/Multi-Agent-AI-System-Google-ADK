import requests

class SpaceXAgent:
    def get_next_launch(self):
        url = "https://api.spacexdata.com/v4/launches/next"
        response = requests.get(url)
        if response.status_code == 200:
            launch = response.json()
            pad_id = launch.get("launchpad")
            pad_url = f"https://api.spacexdata.com/v4/launchpads/{pad_id}"
            pad_response = requests.get(pad_url)
            if pad_response.status_code == 200:
                pad_info = pad_response.json()
                return {
                    "name": launch.get("name"),
                    "date": launch.get("date_utc"),
                    "location": pad_info.get("locality"),
                    "latitude": pad_info.get("latitude"),
                    "longitude": pad_info.get("longitude")
                }
            else:
                return {"error": "Failed to resolve launchpad info"}
        else:
            return {"error": "Failed to fetch SpaceX data"}