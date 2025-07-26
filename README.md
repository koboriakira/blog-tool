# blog-tool

ブログ記事（Markdown）の編集ツール

## 使い方

```
python setup.py sdist
pip install dist/blog_tool-1.0.tar.gz
```

### 既存のタグリストにあるものを付与する

```
# ファイル指定する（指定がない場合は今日のブログ）
blog-tool add_tags --file content/2023/08/05.md
# すべてのファイルに実行
blog-tool add_tags --all
```

### リンクブロックを変換

```
# ファイル指定する（指定がない場合は今日のブログ）
blog-tool bracket --file content/2023/08/05.md
```

### タグを追加

```
blog-tool add_tag --tag {タグ}
```

### タグを削除

```
blog-tool remove_tag --tag {タグ}
```
