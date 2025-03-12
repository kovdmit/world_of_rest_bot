from urllib.parse import urlparse


def get_url(driver):
    current_url = driver.current_url
    parsed_url = urlparse(current_url)

    return parsed_url
