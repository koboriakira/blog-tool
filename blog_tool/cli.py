from blog_tool.get_all_files import get_all_files
from blog_tool.tags import Tags
from blog_tool.remove_tag import handle_remove_tag
from blog_tool.add_tags import handle_add_tags
from blog_tool.add_tag import handle_add_tag
from blog_tool.format_double_brackets import handle_format_double_brackets
import argparse
from datetime import datetime

SUB_COMMANDS = ["remove_tag", "add_tags", "add_tag", "bracket"]
MD_FILES = get_all_files()
ALL_TAGS = Tags.all_tags(md_files=MD_FILES)

parser = argparse.ArgumentParser()
parser.add_argument("sub_command", help="サブコマンドを指定します。",
                    choices=SUB_COMMANDS)
parser.add_argument("--tag", help="タグ指定が必要なコマンドの場合、必要となります")
parser.add_argument("--file", help="ファイル指定が必要なコマンドの場合、必要となります")


def validate_tag(tag) -> None:
    if tag is None:
        print("tagを指定してください")
        exit(1)


def get_file(file) -> str:
    if file is None:
        # 今日の日付をもとに、下のようなファイル名を生成する
        today = datetime.today()
        file = f"/Users/a_kobori/git/blog/content/{today.year}/{today.month:02}/{today.day:02}.md"
    return file


def execute():
    args = parser.parse_args()
    if args.sub_command == "remove_tag":
        validate_tag(args.tag)
        for md_file in MD_FILES:
            handle_remove_tag(md_file=md_file, remove_tag=args.tag)
    elif args.sub_command == "add_tags":
        for md_file in MD_FILES:
            handle_add_tags(md_file=md_file, all_tags=ALL_TAGS)
    elif args.sub_command == "add_tag":
        validate_tag(args.tag)
        for md_file in MD_FILES:
            handle_add_tag(md_file=md_file, tag=args.tag)
    elif args.sub_command == "bracket":
        md_file = get_file(args.file)
        handle_format_double_brackets(md_file=md_file)


if __name__ == "__main__":
    # python -m blog_tool.cli {sub_command}
    # ex.
    # python -m blog_tool.cli remove_tag --tag プロレス
    # python -m blog_tool.cli add_tag --tag "Roam Research"
    # python -m blog_tool.cli bracket
    execute()
