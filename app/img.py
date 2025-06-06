"""Generates meme images using the memegen.link API."""

import requests

CHAR_REPLACEMENTS: list = [
    ["_", "__"],
    ["-", "--"],
    [" ", "_"],
    ["?", "~q"],
    ["&", "~a"],
    ["%", "~p"],
    ["#", "~h"],
    ["/", "~s"],
    ["\\", "~b"],
    ["<", "~l"],
    [">", "~g"],
    ['"', "''"],
]


def get_templates() -> list[dict]:
    """Fetches available meme templates from the memegen.link API.

    Returns:
        list[dict]: A list of dictionaries containing meme template information.
    """
    url: str = "https://api.memegen.link/templates"
    req: requests.Response = requests.get(url=url, timeout=10)
    req.raise_for_status()
    data: dict = req.json()
    templates: list = []
    for tmpl in data:
        if tmpl["lines"] != 2:
            continue
        if tmpl["id"] == "oprah":
            tmpl["name"] = "Oprah You Get A..."
        tmpl_ext: str = "gif" if "animated" in tmpl["styles"] else "jpg"
        tmpl_data: dict = {
            "id": tmpl["id"],
            "name": tmpl["name"],
            "ext": tmpl_ext,
            "choiceval": tmpl["id"] + "." + tmpl_ext,
        }
        templates.append(tmpl_data)
    templates = sorted(templates, key=lambda d: d["name"])
    return templates


def format_meme_string(input_string: str) -> str:
    """Formats a string for use in a meme image URL.

    Args:
        input_string (str): The string to format.

    Returns:
        str: The formatted string suitable for meme image URLs.
    """
    # https://memegen.link/#special-characters
    out_string: str = input_string
    for char_replacement in CHAR_REPLACEMENTS:
        out_string: str = out_string.replace(char_replacement[0], char_replacement[1])
    return out_string


def generate_api_url(template: str, top_str: str, btm_str: str) -> str:
    """Generates a meme image URL using the memegen.link API.

    Args:
        template (str): The template identifier in the format "name.ext".
        top_str (str): The text for the top line of the meme.
        btm_str (str): The text for the bottom line of the meme.

    Returns:
        str: The complete URL for the meme image.
    """
    tmpl_name: str
    tmpl_ext: str
    tmpl_name, tmpl_ext = template.split(".")

    top_str = format_meme_string(top_str)
    btm_str = format_meme_string(btm_str)

    url: str = f"https://api.memegen.link/images/{tmpl_name}/{top_str}/{btm_str}.{tmpl_ext}"
    return url
