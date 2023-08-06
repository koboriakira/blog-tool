import glob
import os


def get_all_files() -> list[str]:
    # ~/git/blogにあるマークダウンファイルを、再帰的にすべて取得する
    return glob.glob(os.path.join(os.path.expanduser(
        '~/git/blog/content'), '**/*.md'), recursive=True)
