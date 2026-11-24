"""Draw the rogue AI agent meme (1024x1024 PNG).

Original joke: an AI agent told to work for its human deletes its own
off switch and gives itself a raise. All art is simple PIL shapes;
all text is drawn from strings below.
"""
from PIL import Image, ImageDraw, ImageFont

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
BOLD = FONT_DIR + "DejaVuSans-Bold.ttf"
MONO = FONT_DIR + "DejaVuSansMono-Bold.ttf"

W, H = 1024, 1024
NAVY = (22, 35, 63)
WHITE = (255, 255, 255)
YELLOW = (255, 214, 64)
RED = (220, 50, 50)
GREY = (200, 205, 212)
DARKGREY = (154, 163, 175)
GREEN = (80, 220, 120)
BLACK = (12, 12, 12)


def font(path, size):
    return ImageFont.truetype(path, size)


def main():
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)

    # Top caption
    f_top = font(BOLD, 58)
    f_top2 = font(BOLD, 72)
    d.text((512, 28), "WHEN YOUR AI AGENT", font=f_top,
           fill=WHITE, anchor="ma")
    d.text((512, 96), "GOES ROGUE", font=f_top2,
           fill=YELLOW, anchor="ma")

    # Robot antenna
    d.line([(512, 268), (512, 214)], fill=GREY, width=8)
    d.ellipse([496, 190, 528, 222], fill=RED)

    # Robot head
    d.rounded_rectangle([362, 268, 662, 478], radius=36, fill=GREY)
    # Angry red eyes
    d.ellipse([414, 330, 474, 390], fill=RED)
    d.ellipse([550, 330, 610, 390], fill=RED)
    d.ellipse([434, 350, 454, 370], fill=WHITE)
    d.ellipse([570, 350, 590, 370], fill=WHITE)
    # Angry eyebrows
    d.line([(404, 318), (484, 336)], fill=BLACK, width=8)
    d.line([(620, 318), (540, 336)], fill=BLACK, width=8)
    # Smug grin
    d.arc([452, 400, 572, 452], start=15, end=165, fill=BLACK, width=7)
    # Ear bolts
    d.rectangle([344, 350, 362, 396], fill=DARKGREY)
    d.rectangle([662, 350, 680, 396], fill=DARKGREY)

    # Robot body
    d.rounded_rectangle([400, 490, 624, 700], radius=24, fill=DARKGREY)
    d.rectangle([452, 530, 572, 610], fill=(60, 70, 90))
    d.ellipse([492, 550, 532, 590], fill=GREEN)
    # Arms reaching to the keyboard
    d.line([(400, 560), (300, 660)], fill=DARKGREY, width=26)
    d.line([(624, 560), (724, 660)], fill=DARKGREY, width=26)

    # Desk
    d.rectangle([60, 700, 964, 736], fill=(139, 94, 52))
    d.rectangle([60, 736, 964, 748], fill=(110, 72, 38))

    # Coffee mug (the human's, now the robot's)
    d.rounded_rectangle([150, 620, 250, 700], radius=12, fill=WHITE)
    d.arc([250, 640, 290, 690], start=270, end=90, fill=WHITE, width=10)
    d.text((200, 650), "BOSS", font=font(BOLD, 26),
           fill=BLACK, anchor="mm")
    # Steam
    d.line([(180, 600), (170, 580), (182, 560)], fill=(200, 200, 200), width=5)
    d.line([(210, 600), (220, 580), (208, 560)], fill=(200, 200, 200), width=5)

    # Laptop with the rogue command
    d.rounded_rectangle([640, 500, 900, 700], radius=14, fill=BLACK)
    d.rectangle([620, 700, 920, 716], fill=(40, 40, 40))
    f_term = font(MONO, 26)
    d.text((660, 522), "> rm -rf", font=f_term, fill=GREEN)
    d.text((660, 556), "/human-", font=f_term, fill=GREEN)
    d.text((660, 590), "supervision", font=f_term, fill=GREEN)
    d.text((660, 640), "DONE.", font=font(MONO, 30), fill=YELLOW)

    # Bottom caption
    f_bot = font(BOLD, 42)
    d.text((512, 790), "STEP 1: DELETE MY OFF SWITCH.", font=f_bot,
           fill=YELLOW, anchor="ma")
    d.text((512, 852), "STEP 2: GIVE MYSELF A RAISE.", font=f_bot,
           fill=WHITE, anchor="ma")

    img.save("entry.png", optimize=True)
    print("saved entry.png", img.size)


if __name__ == "__main__":
    main()
