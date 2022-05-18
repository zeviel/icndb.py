# icndb.py
Web-API for [icndb.com](www.icndb.com) website with jokes about chucknorris

## Example
```python3
import icndb
icndb = icndb.ICNDb()
joke = icndb.generate_random_joke()["value"]["joke"]
print(f"-- Joke::: {joke}")
```
