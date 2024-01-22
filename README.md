# Google Translate URL Transformer

VERY simple python program made in 30 minutes(excuse bugs), Transforms given URL into a Google Translate proxy URL, (theoretically) allowing you to access the content through Google Translate.

## How It Works

The script utilizes the `urllib` library to parse the original URL and then constructs a new URL with Google Translate as a proxy. Translation parameters such as source language (`op`), target language (`en`), and host language (`en-US`) are included to simulate a translation scenario.

## Usage
(make sure to include https:// (common issue))
1. Run the script.
2. Enter the URL you want to transform when prompted.
3. The script will output the original URL and the transformed URL using Google Translate as a proxy.

## Example
```bash python unblock.py
Where do you want to go? https://example.com
Original URL: https://example.com
Transformed URL: https://example-translate-goog.translate.goog/
```
## Multiple Url
In order to transform multiple urls change the usage to the following, add your own input statement if you want.
```bash
# Usage:
url1 = "http://www.google.com"
url2 = "http://www.coolmathgames.com"

transformed_url1 = transform_url(url1)
transformed_url2 = transform_url(url2)

print(f"Original URL 1: {url1}")
print(f"Transformed URL 1: {transformed_url1}")
print()
print(f"Original URL 2: {url2}")
print(f"Transformed URL 2: {transformed_url2}")

# Makes terminal wait for input before closing
input("Press Enter to exit...")
```
