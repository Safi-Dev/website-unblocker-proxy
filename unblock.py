from urllib.parse import urlparse, urlunparse, urlencode

def transform_url(original_url):
    # Parse the original url
    parsed_url = urlparse(original_url)

    # Extract the domain and path
    domain_parts = parsed_url.netloc.split('.')
    domain = '-'.join(domain_parts)
    path = parsed_url.path

    # Create the translation parameters
    translation_params = {
        '_x_tr_sl': 'op',
        '_x_tr_tl': 'en',
        '_x_tr_hl': 'en-US',
        '_x_tr_pto': 'wapp'
    }

    # Add the translation parameters
    new_query = urlencode(translation_params)
    if parsed_url.query:
        new_query = f"{parsed_url.query}&{new_query}"

    # Construct the url
    transformed_url = urlunparse(('https', f'{domain}.translate.goog', path, '', new_query, ''))

    return transformed_url

#Usage:
if __name__ == '__main__':
    url = input("Where you wann go? ")
    transformed_url = transform_url(url)

    print(f"Original URL: {url}")
    print(f"Transformed URL: {transformed_url}")

    # Makes terminal wait for input before closing
    input("Press Enter to exit...")
