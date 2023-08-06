import glob
import os
from blog_tool.tags import Tags


def run():
    # ~/git/blog/contentにあるマークダウンファイルを、再帰的にすべて取得する
    md_files = get_all_file()
    tags = Tags.all_tags(md_files=md_files)

    add_tags(md_file="/Users/a_kobori/git/blog-tool/test.md",
             tags=tags)


def add_tags(md_file: str, tags: Tags) -> None:
    tag_values = tags.values.copy()
    tags_line_idx = 0
    content_tags = Tags(values=[])
    with open(md_file, 'r') as f:
        lines = f.readlines()
        for idx, line in enumerate(lines):
            # "tags:"から始まる場合、その行に含まれるタグ名を取得する
            if line.startswith("tags:"):
                # idxを覚えておく
                tags_line_idx = idx
                # タグ(tag)をリンクに変換する
                content_tags = content_tags.add(Tags.from_string(line))
                # あらかじめそのタグたちはリンクになっているので、リストから削除する
                tag_values = [
                    tag for tag in tag_values if tag not in content_tags.values]
            for tag in tag_values:
                # title: から始まる行は無視
                if line.startswith("title:"):
                    continue
                # タグ(tag)が含まれる文章(line)であるかを判定
                if tag in line:
                    # すでにタグ(tag)がリンクになっていないかを判定。
                    # リンクとは[Notion](/tags/Notion)のようなものを指す
                    if not f"[{tag}](/tags/{tag})" in line:
                        # タグ(tag)をリンクに変換する
                        lines[idx] = lines[idx].replace(
                            tag, f"[{tag}](/tags/{tag})", 1)
                        # タグ(tag)を追加したので、リストから削除する
                        tag_values.remove(tag)
                        content_tags = content_tags.add_tag(tag)
        # tags:の行を更新する
        lines[tags_line_idx] = f"tags: {content_tags.to_blog_string()}\n"
        print("".join(lines))


def get_all_file() -> list[str]:
    # ~/git/blogにあるマークダウンファイルを、再帰的にすべて取得する
    return glob.glob(os.path.join(os.path.expanduser(
        '~/git/blog/content'), '**/*.md'), recursive=True)


if __name__ == '__main__':
    run()
