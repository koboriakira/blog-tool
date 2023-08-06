from blog_tool.tags import Tags


def handle_add_tag(md_file: str, tag: str) -> None:
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
                # すでに追加したいタグがある場合は、何もしない
                if tag in content_tags.values:
                    return
            # タグ(tag)が含まれる文章(line)であるかを判定
            if tag in line:
                # リンクを生成。半角スペースはエスケープする
                link = f"[{tag}](/tags/{tag.replace(' ', '%20')})"

                # すでにタグ(tag)がリンクになっていないかを判定。
                if not link in line:
                    # タグ(tag)をリンクに変換する
                    lines[idx] = lines[idx].replace(
                        tag, link, 1)
                    # tags:の行を更新する
                    content_tags = content_tags.add_tag(tag)
                    lines[tags_line_idx] = f"tags: {content_tags.to_blog_string()}\n"
                    break

        # ファイルを更新
        with open(md_file, 'w') as f:
            f.writelines(lines)
