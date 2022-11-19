from requests import get

class ICNDB:
	def __init__(self) -> None:
		self.api = "https://api.icndb.com"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
		}

	def get_random_joke(
			self,
			count: int = 1,
			first_name: str = None,
			last_name: str = None,
			limit_to: str = "nerdy",
			exclude: str = None) -> dict:
		url = f"{self.api}/jokes/random/{count}?limitTo=[{limit_to}]"
		if first_name:
			url += f"&firstName={first_name}"
		if last_name:
			url += f"&lastName={last_name}"
		if exclude:
			url += f"&exclude=[{exclude}]"
		return get(
			url,
			headers=self.headers,
			verify=False).json()

	def get_specific_joke(self, id: int) -> dict:
		return get(
			f"{self.api}/jokes/{id}",
			headers=self.headers,
			verify=False).json()

	def get_jokes_count(self) -> dict:
		return get(
			f"{self.api}/jokes/count",
			headers=self.headers,
			verify=False).json()

	def get_joke_categories(self) -> dict:
		return get(
			f"{self.api}/categories",
			headers=self.headers,
			verify=False).json()

	def get_all_jokes(self) -> dict:
		return get(
			f"{self.api}",
			headers=self.headers,
			verify=False).json()
