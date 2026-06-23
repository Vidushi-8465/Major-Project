import json


files = [

    "data/parsed_chunks/file_chunks.json",

    "data/parsed_chunks/class_chunks.json",

    "data/parsed_chunks/function_chunks.json"

]


for file in files:

    with open(
        file,
        "r",
        encoding="utf-8"
    ) as f:

        data = json.load(f)

    avg_size = (
        sum(
            len(
                item["content"]
            )
            for item in data
        )
        /
        len(data)
    )

    print(
        f"\n{file}"
    )

    print(
        f"Chunks: {len(data)}"
    )

    print(
        f"Average Size: "
        f"{avg_size:.2f}"
    )