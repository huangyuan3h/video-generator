import requests
from PIL import Image, ImageDraw, ImageFont
import qrcode
import textwrap

from task.images.pexels import get_top_photo
from task.utils import get_image_path


def create_video_cover(title, qr_text, output_path="cover.jpg", orientation="landscape", background_image_path=None):
    # 封面尺寸设置
    width, height = (1280, 720) if orientation == "landscape" else (720, 1280)

    # 如果有背景图片，则加载并调整大小
    if background_image_path:
        cover = Image.open(background_image_path).convert("RGB")
        cover = cover.resize((width, height), Image.LANCZOS)
    else:
        cover = Image.new("RGB", (width, height), color=(30, 30, 30))  # 深灰背景

    draw = ImageDraw.Draw(cover)
    title_font = ImageFont.truetype("resources/fonts/NotoSansSC-Bold.ttf", 60)  # 根据需要更换字体

    # 根据封面宽度自动换行
    max_width = width - 200  # 留出左右100像素边距
    wrapped_title = []
    for line in title.split('\n'):
        wrapped_title.extend(textwrap.wrap(line, width=int(max_width / title_font.getbbox('A')[2])))

    # 计算多行文本总高度以居中
    total_text_height = sum([title_font.getbbox(line)[3] - title_font.getbbox(line)[1] for line in wrapped_title]) + (
            len(wrapped_title) - 1) * 10  # 行间距10
    current_y = (height - total_text_height) // 2  # 竖直方向居中

    # 绘制多行文本
    for line in wrapped_title:
        line_width = title_font.getbbox(line)[2] - title_font.getbbox(line)[0]
        line_x = (width - line_width) // 2
        draw.text((line_x, current_y), line, font=title_font, fill="white")
        current_y += title_font.getbbox(line)[3] - title_font.getbbox(line)[1] + 10  # 行间距10像素

    # 生成二维码
    qr = qrcode.QRCode(box_size=10, border=2)
    qr.add_data(qr_text)
    qr.make(fit=True)
    qr_img = qr.make_image(fill="black", back_color="white").convert("RGB")

    # 调整二维码大小并粘贴到封面
    qr_size = 150  # 二维码大小
    qr_img = qr_img.resize((qr_size, qr_size), Image.LANCZOS)
    qr_position = (width - qr_size - 30, height - qr_size - 30)  # 右下角位置，留 30 像素边距
    cover.paste(qr_img, qr_position)

    # 保存封面图像
    cover.save(output_path)
    print(f"封面已保存至 {output_path}")


def download_image(image_url, save_path):
    """
    Download an image from a URL and save it to a specified location.

    :param image_url: The URL of the image.
    :param save_path: The path where the image will be saved, including the filename and extension.
    """
    try:
        # Send a GET request to fetch the image content
        response = requests.get(image_url)

        # Check if the request was successful
        if response.status_code == 200:
            # Open the file in binary write mode and save the image content
            with open(save_path, 'wb') as file:
                file.write(response.content)
            print(f"Image saved to {save_path}")
        else:
            print(f"Failed to download image. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")


def build_cover_image(title,qr_text,  query, task_id, orientation="landscape"):
    url = get_top_photo(query, orientation)
    photo_path = get_image_path(task_id, orientation)
    download_image(url, photo_path)

    create_video_cover(title, qr_text, output_path=photo_path, orientation=orientation, background_image_path=photo_path)