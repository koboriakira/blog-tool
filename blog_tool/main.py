import glob
import os
from blog_tool.tags import Tags
from get_all_files import get_all_files

MD_FILES = get_all_files()
ALL_TAGS = Tags.all_tags(md_files=MD_FILES)


def run():
    # ~/git/blog/contentにあるマークダウンファイルを、再帰的にすべて取得する

    # add_tags(md_file="/Users/a_kobori/git/blog-tool/test.md")
    remove_tag(md_file="/Users/a_kobori/git/blog-tool/test.md",
               remove_tag="Notion")


def remove_tag(md_file: str, remove_tag: str) -> None:
    with open(md_file, 'r') as f:
        lines = f.readlines()
        for idx, line in enumerate(lines):
            # title: から始まる行は無視
            if line.startswith("title:"):
                continue
            # "tags:"から始まる場合、その行に含まれるタグ名を取得する
            if line.startswith("tags:"):
                # タグ(tag)をリンクに変換する
                content_tags = Tags.from_string(line)
                content_tags = content_tags.remove_tag(remove_tag)
                lines[idx] = f"tags: {content_tags.to_blog_string()}\n"
            if remove_tag in line:
                # すでにタグ(tag)がリンクになっていないかを判定。
                # リンクとは[Notion](/tags/Notion)のようなものを指す
                if f"[{remove_tag}](/tags/{remove_tag})" in line:
                    # タグ(tag)を通常の文字列に変換する
                    lines[idx] = lines[idx].replace(
                        f"[{remove_tag}](/tags/{remove_tag})", remove_tag)
        print("".join(lines))


def add_tags(md_file: str) -> None:
    tag_values = ALL_TAGS.values.copy()
    tags_line_idx = 0
    content_tags = Tags(values=[])
    with open(md_file, 'r') as f:
        lines = f.readlines()
        for idx, line in enumerate(lines):
            # title: から始まる行は無視
            if line.startswith("title:"):
                continue
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
