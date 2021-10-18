import qrcode
from qrcode.image.pil import PilImage


def qr_code(url: str, box_size=4, border=4, fill_color=(255, 153, 51), back_color=(255, 255, 255)) -> PilImage:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.ERROR_CORRECT_L,
        box_size=box_size,
        border=border
    )

    qr.add_data(url)
    qr.make(fit=True)

    return qr.make_image(fill_color=fill_color, back_color=back_color)
