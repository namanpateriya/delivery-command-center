import json

from pathlib import Path


def load_json_file(
    file_path: str
):

    path = Path(
        file_path
    )

    if not path.exists():

        raise FileNotFoundError(
            (
                f"JSON file not found: "
                f"{file_path}"
            )
        )

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(
            file
        )
