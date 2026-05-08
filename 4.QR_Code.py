import qrcode

urls = input("Enter the list of urls to generate the qrcode: \t")
file_name = input("Enter the list of names to generate the qrcode: \t")

img = qrcode.make(urls)

img.save(f"{file_name}.png")

print("QR generated")

    