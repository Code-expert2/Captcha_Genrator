from io import BytesIO
from tkinter import *
from random import randint
from tkinter import messagebox
import string
from captcha.image import ImageCaptcha

# Update font paths for Linux
image = ImageCaptcha(fonts=['/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', '/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf'])

# Generate a random 6-digit number
random_code = str(randint(100000, 999999))
image_data = image.generate(random_code)
assert isinstance(image_data, BytesIO)
image.write(random_code, 'captcha.png')

def verify():
    global random_code
    user_input = t1.get("1.0", END).strip()
    if user_input == random_code:
        messagebox.showinfo("Success", "Captcha Verified!")
    else:
        messagebox.showwarning("Error", "Incorrect Captcha!")
        refresh()

def refresh():
    global random_code
    random_code = str(randint(100000, 999999))
    image_data = image.generate(random_code)
    assert isinstance(image_data, BytesIO)
    image.write(random_code, 'captcha.png')
    
    # Update image in Tkinter
    new_photo = PhotoImage(file="captcha.png")
    l1.config(image=new_photo)
    l1.image = new_photo  # Keep reference to avoid garbage collection

# Initialize GUI
root = Tk()
root.title("Captcha Verification")

photo = PhotoImage(file="captcha.png")

l1 = Label(root, image=photo, height=100, width=200)
t1 = Text(root, height=2, width=15)
b1 = Button(root, text="Submit", command=verify)
b2 = Button(root, text="Refresh", command=refresh)

# Layout
l1.pack(pady=10)
t1.pack(pady=5)
b1.pack(pady=5)
b2.pack(pady=5)

root.mainloop()
