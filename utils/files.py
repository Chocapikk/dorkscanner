import os


def load_dorks(fname: str) -> list[str]:
    """Load a list of dork queries from a file.\n
    Args:
        str: full / relative path to file in cwd
    Return:
        list[str]:  list of dork strings
    """
    if fname[0] == "~":
        # Expand relative path
        fname = os.path.expanduser(fname)
    elif fname[0] != "/":
        # Assume path in cwd
        fname = f"{os.getcwd()}/{fname}"
    if os.path.isfile(fname):
        with open(fname, "r", encoding="utf8") as file:
            lines = [q.strip() for q in file.readlines()]
            return lines
    else:
        raise FileNotFoundError(f"File {fname} doesn't exist")
