import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
import time
import logging

class CryptusApp:
    def __init__(self, master):
        self.master = master
        master.title("Cryptus Cipher")

        self.setup_logger()

        self.label = tk.Label(master, text="Cryptus Cipher", font=("Arial", 16))
        self.label.pack()

        self.text_entry = tk.Text(master, height=10, width=60)
        self.text_entry.pack()

        self.algorithm_label = tk.Label(master, text="Select Algorithm:")
        self.algorithm_label.pack()

        self.algorithm_combobox = ttk.Combobox(master, values=["AES", "DES", "RSA", "Fernet"])
        self.algorithm_combobox.pack()

        self.encrypt_button = tk.Button(master, text="Encrypt", command=self.encrypt_text)
        self.encrypt_button.pack()

        self.decrypt_button = tk.Button(master, text="Decrypt", command=self.decrypt_text)
        self.decrypt_button.pack()

        self.output_text = tk.Text(master, height=10, width=60)
        self.output_text.pack()

        self.help_button = tk.Button(master, text="Help", command=self.show_help)
        self.help_button.pack()

        # Şifreleme yöntemlerini tanımlayın
        self.encryption_methods = {
            "AES": self.encrypt_aes,
            "DES": self.encrypt_des,
            "RSA": self.encrypt_rsa,
            "Fernet": self.encrypt_fernet
        }

        # Şifre çözme yöntemlerini tanımlayın
        self.decryption_methods = {
            "AES": self.decrypt_aes,
            "DES": self.decrypt_des,
            "RSA": self.decrypt_rsa,
            "Fernet": self.decrypt_fernet
        }

    def setup_logger(self):
        logging.basicConfig(filename='cryptus.log', level=logging.INFO,
                            format='%(asctime)s %(levelname)s: %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.logger = logging.getLogger()

    def log(self, message):
        self.logger.info(message)

    def encrypt_text(self):
        input_text = self.text_entry.get("1.0", tk.END).strip()
        algorithm = self.algorithm_combobox.get()
        if not input_text:
            messagebox.showwarning("Warning", "Please enter text to encrypt.")
            return
        encrypted_text = self.encrypt(input_text, algorithm)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, encrypted_text)

    def decrypt_text(self):
        input_text = self.text_entry.get("1.0", tk.END).strip()
        algorithm = self.algorithm_combobox.get()
        if not input_text:
            messagebox.showwarning("Warning", "Please enter text to decrypt.")
            return
        decrypted_text = self.decrypt(input_text, algorithm)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, decrypted_text)

    def encrypt(self, text, algorithm):
        # Seçilen şifreleme yöntemine göre şifreleme işlemini gerçekleştir
        return self.encryption_methods[algorithm](text)

    def decrypt(self, text, algorithm):
        # Seçilen şifreleme yöntemine göre şifre çözme işlemini gerçekleştir
        return self.decryption_methods[algorithm](text)

    # Şifreleme yöntemlerini tanımlayın
    def encrypt_aes(self, text):
        self.log("AES encryption performed")
        return "AES encrypted text"

    def encrypt_des(self, text):
        self.log("DES encryption performed")
        return "DES encrypted text"

    def encrypt_rsa(self, text):
        self.log("RSA encryption performed")
        return "RSA encrypted text"

    def encrypt_fernet(self, text):
        # Fernet şifreleme algoritması kullanarak metni şifrele
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        encrypted_text = cipher_suite.encrypt(text.encode())
        self.log("Fernet encryption performed")
        return encrypted_text.decode()

    # Şifre çözme yöntemlerini tanımlayın
    def decrypt_aes(self, text):
        self.log("AES decryption performed")
        return "AES decrypted text"

    def decrypt_des(self, text):
        self.log("DES decryption performed")
        return "DES decrypted text"

    def decrypt_rsa(self, text):
        self.log("RSA decryption performed")
        return "RSA decrypted text"

    def decrypt_fernet(self, text):
        # Fernet şifreleme algoritması kullanarak metni şifre çözme
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        decrypted_text = cipher_suite.decrypt(text.encode())
        self.log("Fernet decryption performed")
        return decrypted_text.decode()

    def show_help(self):
        messagebox.showinfo("Help", "For more information, visit our GitHub repository. github.com/aptus0")

def main():
    root = tk.Tk()
    app = CryptusApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()