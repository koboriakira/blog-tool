from dataclasses import dataclass


class Tags:
    values: list[str]

    def __init__(self, values: list[str]):
        self.values = list(set(values))
        # 空文字の要素を削除する
        self.values = [value for value in self.values if value != ""]

    def add(self, tags: 'Tags') -> 'Tags':
        return Tags(values=self.values + tags.values)

    def add_tag(self, tag: str) -> 'Tags':
        return Tags(values=self.values + [tag])

    def remove_tag(self, tag: str) -> 'Tags':
        return Tags(values=[value for value in self.values if value != tag])

    def to_blog_string(self) -> str:
        # ダブルクオーテーションで囲む
        values = [f"\"{value}\"" for value in self.values]
        return f"[{', '.join(values)}]"

    @ staticmethod
    def all_tags(md_files: list[str]) -> 'Tags':
        tags = Tags(values=[])
        for md_file in md_files:
            # マークダウンファイルを読み込む
            with open(md_file, 'r') as f:
                for line in f.readlines():
                    # "tags:"から始まる場合、その行に含まれるタグ名を取得する
                    if line.startswith("tags:"):
                        tags = tags.add(Tags.from_string(line))
        return tags

    @ staticmethod
    def from_string(input: str) -> 'Tags':
        values = input.replace("tags:", "").replace(
            "[", "").replace(
            "]", "").split(",")
        values = [v.strip().replace("\"", "") for v in values]
        return Tags(values=values)
