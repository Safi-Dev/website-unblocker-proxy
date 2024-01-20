# Google Translate URL Transformer

VERY simple python program made in 30 minutes(excuse bugs), Transforms given URL into a Google Translate proxy URL, allowing you to access the content through Google Translate.

## How It Works

The script utilizes the `urllib` library to parse the original URL and then constructs a new URL with Google Translate as a proxy. Translation parameters such as source language (`op`), target language (`en`), and host language (`en-US`) are included to simulate a translation scenario.

## Usage
1. Run the script.
2. Enter the URL you want to transform when prompted.
3. The script will output the original URL and the transformed URL using Google Translate as a proxy.

## Example
```bash python unblock.py
Where do you want to go? [https://exam,](https://example.com)
Original URL: https://example.com
Transformed URL: https://example-translate-goog.translate.goog/
