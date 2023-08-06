from blog_tool.tags import Tags


def handle_remove_tag(md_file: str, remove_tag: str) -> None:
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
                removed_content_tags = content_tags.remove_tag(remove_tag)
                if not removed_content_tags.equals(content_tags):
                    lines[idx] = f"tags: {removed_content_tags.to_blog_string()}\n"
            if remove_tag in line:
                # すでにタグ(tag)がリンクになっていないかを判定。
                # リンクとは[Notion](/tags/Notion)のようなものを指す
                if f"[{remove_tag}](/tags/{remove_tag})" in line:
                    # タグ(tag)を通常の文字列に変換する
                    lines[idx] = lines[idx].replace(
                        f"[{remove_tag}](/tags/{remove_tag})", remove_tag)
        # ファイルを更新
        with open(md_file, 'w') as f:
            f.writelines(lines)
