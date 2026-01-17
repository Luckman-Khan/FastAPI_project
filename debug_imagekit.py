from imagekitio import ImageKit
import inspect
import os
from dotenv import load_dotenv

load_dotenv()

print("Env vars present:")
print("IMAGEKIT_PUBLIC_KEY:", "Yes" if os.getenv("IMAGEKIT_PUBLIC_KEY") else "No")
print("IMAGEKIT_PRIVATE_KEY:", "Yes" if os.getenv("IMAGEKIT_PRIVATE_KEY") else "No")
print("IMAGEKIT_URL:", "Yes" if os.getenv("IMAGEKIT_URL") else "No")

print("\nImageKit Init Signature:")
try:
    print("Signature:", inspect.signature(ImageKit.__init__))
except Exception as e:
    print("Could not get signature:", e)

print("\nTrying to init with camelCase:")
try:
    imagekit = ImageKit(
        publicKey="dummy_public",
        privateKey="dummy_private",
        urlEndpoint="dummy_url"
    )
    print("Init successful with camelCase")
except Exception as e:
    print("Init with camelCase failed:", e)

print("\nTrying to init with positional (if possible):")
try:
    # Just guessing order if positional: public, private, url
    imagekit = ImageKit(
        "dummy_public",
        "dummy_private",
        "dummy_url"
    )
    print("Init successful with positional")
except Exception as e:
    print("Init with positional failed:", e)
