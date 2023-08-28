from blog_tool.tags import Tags


def handle_add_tags(md_file: str, all_tags: Tags) -> None:
    tag_values = all_tags.values.copy()
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
                    tag_element = _create_tag_element(tag)
                    if not tag_element in line:
                        # タグ(tag)をリンクに変換する
                        lines[idx] = lines[idx].replace(tag, tag_element, 1)
                        # タグ(tag)を追加したので、リストから削除する
                        tag_values.remove(tag)
                        content_tags = content_tags.add_tag(tag)
        # tags:の行を更新する
        lines[tags_line_idx] = f"tags: {content_tags.to_blog_string()}\n"

        # ファイルを更新
        with open(md_file, 'w') as f:
            f.writelines(lines)

def _create_tag_element(tag: str) -> str:
    return f"[{tag}](/tags/{tag.replace(' ', '%20')})"
