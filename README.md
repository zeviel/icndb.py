# icndb.py
Web-API for [icndb.com](https://www.icndb.com) website with jokes about chucknorris

## Example
```python3
import icndb
icndb = icndb.ICNDB()
joke = icndb.generate_random_joke()["value"]["joke"]
print(joke)
```
