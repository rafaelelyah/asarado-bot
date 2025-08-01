def update_version(tags: list, current_version="v0.0.0"):
    major, minor, patch = map(int, current_version[1:].split("."))

    if "MAJOR" in tags:
        major += 1
        minor = 0
        patch = 0
    elif "MINOR" in tags:
        minor += 1
        patch = 0
    elif "PATCH" in tags:
        patch += 1

    return f"v{major}.{minor}.{patch}"