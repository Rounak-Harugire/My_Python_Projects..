import qrcode
qr = qrcode.make('HELLO IM ROUNAK...')
qr.save('qr.png')
print('QR code is generated.')