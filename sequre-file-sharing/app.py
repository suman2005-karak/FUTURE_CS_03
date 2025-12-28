from flask import Flask, render_template, request, redirect, url_for, send_file
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from werkzeug.utils import secure_filename
from pathlib import Path
import os

app = Flask(__name__)

# ---------------- CONFIG ----------------
UPLOAD_FOLDER = "uploads"
ENCRYPTED_FOLDER = "encrypted_files"
KEY_FILE = "secret.key"

Path(UPLOAD_FOLDER).mkdir(exist_ok=True)
Path(ENCRYPTED_FOLDER).mkdir(exist_ok=True)


# ---------------- KEY MANAGEMENT ----------------
def load_key():
    """
    Strict key loading.
    If key is missing → FAIL (no auto regeneration)
    """
    key_path = Path(KEY_FILE)
    if not key_path.exists():
        raise FileNotFoundError("Encryption key missing")
    return key_path.read_bytes()


def generate_key_once():
    """
    Run ONLY ONCE during initial setup.
    """
    key_path = Path(KEY_FILE)
    if not key_path.exists():
        key = get_random_bytes(32)  # AES-256
        key_path.write_bytes(key)
        print("Encryption key generated.")


# Generate key only if it does not exist (initial setup)
generate_key_once()


# ---------------- ENCRYPTION ----------------
def encrypt_file(data: bytes) -> bytes:
    key = load_key()
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return cipher.nonce + tag + ciphertext


def decrypt_file(data: bytes) -> bytes:
    key = load_key()
    nonce = data[:16]
    tag = data[16:32]
    ciphertext = data[32:]

    cipher = AES.new(key, AES.MODE_EAX, nonce)
    return cipher.decrypt_and_verify(ciphertext, tag)


# ---------------- ROUTES ----------------
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        if "file" not in request.files:
            return "No file part", 400

        file = request.files["file"]

        if file.filename == "":
            return "No file selected", 400

        filename = secure_filename(file.filename)
        data = file.read()

        if not data:
            return "Empty file not allowed", 400

        try:
            encrypted_data = encrypt_file(data)
        except FileNotFoundError:
            return "Encryption key missing", 500
        except Exception:
            return "Encryption failed", 500

        encrypted_path = Path(ENCRYPTED_FOLDER) / f"{filename}.enc"
        encrypted_path.write_bytes(encrypted_data)

        return redirect(url_for("success", filename=filename))

    return render_template("index.html")


@app.route("/success/<filename>")
def success(filename):
    filename = secure_filename(filename)
    return render_template("success.html", filename=filename)


@app.route("/download/<filename>")
def download(filename):
    filename = secure_filename(filename)

    encrypted_path = Path(ENCRYPTED_FOLDER) / f"{filename}.enc"
    decrypted_path = Path(UPLOAD_FOLDER) / filename

    if not encrypted_path.exists():
        return "Encrypted file not found", 404

    try:
        encrypted_data = encrypted_path.read_bytes()
        decrypted_data = decrypt_file(encrypted_data)

        decrypted_path.write_bytes(decrypted_data)

        return send_file(
            decrypted_path,
            as_attachment=True,
            download_name=filename
        )

    except FileNotFoundError:
        return "Encryption key missing", 500
    except ValueError:
        return "Decryption failed (wrong key or tampered file)", 500
    except Exception:
        return "Internal server error", 500


@app.route("/files")
def list_files():
    files = [f.stem for f in Path(ENCRYPTED_FOLDER).glob("*.enc")]
    return render_template("files.html", files=files)


# ---------------- MAIN ----------------
if __name__ == "__main__":
    app.run(debug=False, host="127.0.0.1", port=5000)
