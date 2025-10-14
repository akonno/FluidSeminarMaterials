import argparse
import base64
import os
import sys

def image_to_markdown(path):
    """
    画像ファイルをBase64エンコードし、Colab/Jupyter互換のMarkdown表記に変換する。
    例: ![filename.png](data:image/png;base64,....)
    """
    ext = os.path.splitext(path)[1].lower()
    mime = {
        '.png': 'image/png',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.gif': 'image/gif',
        '.svg': 'image/svg+xml'
    }.get(ext, 'application/octet-stream')

    # ファイル読み込みとBase64エンコード（改行なし）
    with open(path, "rb") as f:
        b64data = base64.b64encode(f.read()).decode('utf-8')

    markdown = f"![{os.path.basename(path)}](data:{mime};base64,{b64data})"
    return markdown


def main():
    parser = argparse.ArgumentParser(
        description="Convert an image file to Markdown (Base64-embedded) format for Jupyter/Colab."
    )
    parser.add_argument("image", help="Path to the image file (e.g., sample.png)")
    args = parser.parse_args()

    if not os.path.isfile(args.image):
        print(f"Error: File not found: {args.image}", file=sys.stderr)
        sys.exit(1)

    markdown = image_to_markdown(args.image)
    print(markdown)  # コピペしやすいように標準出力へ


if __name__ == "__main__":
    main()
