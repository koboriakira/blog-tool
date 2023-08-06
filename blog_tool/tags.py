from dataclasses import dataclass


class Tags:
    values: list[str]

    def __init__(self, values: list[str]):
        self.values = list(set(values))
        # 空文字の要素を削除する
        self.values = [value for value in self.values if value != ""]

    @staticmethod
    def from_string(input: str) -> 'Tags':
        values = input.replace("tags:", "").replace(
            "[", "").replace(
            "]", "").split(",")
        values = [v.strip().replace("\"", "") for v in values]
        return Tags(values=values)
