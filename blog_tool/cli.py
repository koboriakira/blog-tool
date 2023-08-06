from blog_tool.get_all_files import get_all_files
from blog_tool.tags import Tags
from blog_tool.remove_tag import handle_remove_tag
from blog_tool.add_tags import handle_add_tags
import argparse

MD_FILES = get_all_files()
ALL_TAGS = Tags.all_tags(md_files=MD_FILES)

parser = argparse.ArgumentParser()
parser.add_argument("sub_command", help="サブコマンドを指定します。",
                    choices=["remove_tag", "add_tags"])
parser.add_argument("--tag", help="タグ指定が必要なコマンドの場合、必要となります")


def remove_tag(tag: str):
    for md_file in MD_FILES:
        handle_remove_tag(md_file=md_file, remove_tag=tag)


def add_tags():
    for md_file in MD_FILES:
        handle_add_tags(md_file=md_file, all_tags=ALL_TAGS)


def execute():
    args = parser.parse_args()
    if args.sub_command == "remove_tag":
        if args.tag is None:
            print("tagを指定してください")
            exit(1)
        remove_tag(args.tag)
    elif args.sub_command == "add_tags":
        add_tags()


if __name__ == "__main__":
    # python -m blog_tool.cli {sub_command}
    # ex.
    # python -m blog_tool.cli remove_tag --tag=プロレス
    execute()
