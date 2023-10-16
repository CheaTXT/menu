import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=20,
    border=2,
)

# Add your data to the QR code
data = "https://crafted-menu.onrender.com"
qr.add_data(data)

# Make the QR code
qr.make(fit=True)

# Create the QR code image with specified fill and background colors
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
img.save("menu.png")
