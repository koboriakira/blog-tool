from blog_tool.tags import Tags


def handle_format_double_brackets(md_file: str) -> None:
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

            # [[と]]で囲まれた文字列を取得する
            start_idx = line.find("[[")
            end_idx = line.find("]]")
            if start_idx != -1 and end_idx != -1:
                # タグ(tag)をリンクに変換する
                tag = line[start_idx + 2:end_idx]
                # タグ(tag)をリンクに変換する
                lines[idx] = lines[idx].replace(
                    f"[[{tag}]]", f"[{tag}](/tags/{tag.replace(' ', '%20')})", 1)
                # tags:の行を更新する
                content_tags = content_tags.add_tag(tag)

        # tags:の行を更新する
        lines[tags_line_idx] = f"tags: {content_tags.to_blog_string()}\n"

        # ファイルを更新
        with open(md_file, 'w') as f:
            f.writelines(lines)
