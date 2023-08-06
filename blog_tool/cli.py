from blog_tool.get_all_files import get_all_files
from blog_tool.tags import Tags
from blog_tool.remove_tag import handle_remove_tag
from blog_tool.add_tags import handle_add_tags
from blog_tool.add_tag import handle_add_tag
import argparse

SUB_COMMANDS = ["remove_tag", "add_tags", "add_tag"]
MD_FILES = get_all_files()
ALL_TAGS = Tags.all_tags(md_files=MD_FILES)

parser = argparse.ArgumentParser()
parser.add_argument("sub_command", help="サブコマンドを指定します。",
                    choices=SUB_COMMANDS)
parser.add_argument("--tag", help="タグ指定が必要なコマンドの場合、必要となります")


def remove_tag(tag: str):
    for md_file in MD_FILES:
        handle_remove_tag(md_file=md_file, remove_tag=tag)


def add_tags():
    for md_file in MD_FILES:
        handle_add_tags(md_file=md_file, all_tags=ALL_TAGS)


def add_tag(tag: str):
    # handle_add_tag(md_file="/Users/a_kobori/git/blog-tool/test.md", tag=tag)
    for md_file in MD_FILES:
        handle_add_tag(md_file=md_file, tag=tag)


def validate_tag(tag) -> None:
    if tag is None:
        print("tagを指定してください")
        exit(1)


def execute():
    args = parser.parse_args()
    if args.sub_command == "remove_tag":
        validate_tag(args.tag)
        remove_tag(args.tag)
    elif args.sub_command == "add_tags":
        add_tags()
    elif args.sub_command == "add_tag":
        validate_tag(args.tag)
        add_tag(args.tag)


if __name__ == "__main__":
    # python -m blog_tool.cli {sub_command}
    # ex.
    # python -m blog_tool.cli remove_tag --tag プロレス
    # python -m blog_tool.cli add_tag --tag "Roam Research"
    execute()
