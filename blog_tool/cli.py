from blog_tool.get_all_files import get_all_files
from blog_tool.tags import Tags
from blog_tool.remove_tag import handle_remove_tag
import argparse

MD_FILES = get_all_files()
ALL_TAGS = Tags.all_tags(md_files=MD_FILES)

parser = argparse.ArgumentParser()
parser.add_argument("sub_command", help="サブコマンドを指定します。",
                    choices=["remove_tag"])
parser.add_argument("--tag", help="タグ指定が必要なコマンドの場合、必要となります")


def remove_tag(tag: str):
    handle_remove_tag(
        md_file="/Users/a_kobori/git/blog-tool/test.md", remove_tag=tag)


def execute():
    args = parser.parse_args()
    if args.sub_command == "remove_tag":
        if args.tag is None:
            print("tagを指定してください")
            exit(1)
        remove_tag(args.tag)


if __name__ == "__main__":
    # python -m blog_tool.cli {sub_command}
    execute()
