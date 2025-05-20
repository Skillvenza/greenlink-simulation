
from stegano import lsb
import base64
import os

def embed_url(input_image_path, target_url, output_image_path):
    try:
        print(f"[*] Embedding URL into: {input_image_path}")
        encoded_url = base64.b64encode(target_url.encode()).decode()
        secret_image = lsb.hide(input_image_path, encoded_url)
        secret_image.save(output_image_path)
        print(f"[+] URL successfully embedded into {output_image_path}")
    except Exception as e:
        print(f"[!] Failed to embed URL: {e}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Embed a URL into an image using steganography.")
    parser.add_argument("--in", dest="input_image", required=True, help="Path to input image")
    parser.add_argument("--url", dest="url", required=True, help="URL to embed")
    parser.add_argument("--out", dest="output_image", required=True, help="Path to output image")
    args = parser.parse_args()

    embed_url(args.input_image, args.url, args.output_image)
