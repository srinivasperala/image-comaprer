#!/usr/bin/env python
import glob
from sys import argv
from PIL import Image


def DifferenceHash(theImage):

    theImage = theImage.resize((8, 8), Image.ANTIALIAS)

    theImage = theImage.convert("L")

    previousPixel = theImage.getpixel((0, 7))

    differenceHash = 0

    for row in range(0, 8, 2):

        for col in range(8):
            differenceHash <<= 1
            pixel = theImage.getpixel((col, row))
            differenceHash |= 1 * (pixel >= previousPixel)
            previousPixel = pixel

        row += 1

        for col in range(7, -1, -1):
            differenceHash <<= 1
            pixel = theImage.getpixel((col, row))
            differenceHash |= 1 * (pixel >= previousPixel)
            previousPixel = pixel

    return differenceHash

def loadImage(filename):
    try:
        theImage = Image.open(filename)
        theImage.load()
        return theImage
    except:
        print("\nCouldn't open the image " + filename + ".\n")
        raise Exception('OpenError')

def isImage(filename):
    if filename.endswith(('.jpg', '.JPG', '.jpeg', 'JPEG', '.png', '.PNG', 'gif', 'GIF')):
        return True
    return False

# Executing file using:
#         argv[0]     argv[1]        argv[2]              argv[3]       argv[4]                     argv[5]
# python3 szperacz.py <pattern_path> <img_to_change_path> <search_path> <txt_file_with_changes_log> <allowed_changes_in_%>
if __name__ == '__main__':

    if len(argv) == 6:
        x = 0
        for i in argv:
            print(str(x) + ": " + i)
            x += 1
        log_file = open(argv[4], 'a')
        f = Image.open(argv[2])
        image1 = loadImage(argv[1])
        hash1 = DifferenceHash(image1)
        print("\n" + argv[1] + "\t%(hash)016x" % {"hash": hash1})
        for filename in glob.iglob(argv[3].rstrip('/')+'/**/*.*', recursive=True):
            if isImage(filename):
                try:
                    image2 = loadImage(filename)
                except:
                    nf = open('error_log.txt', 'a')
                    nf.write("ERROR with file: " + filename + "\n")
                    continue
                hash2 = DifferenceHash(image2)
                similarity = ((64 - bin(hash1 ^ hash2).count("1")) * 100.0) / 64.0
                if similarity >= float(argv[5]):
                    print("\n" + filename + " " + str(similarity) + "\t%(hash)016x" % {"hash": hash2})
                    f.save(filename)
                    print(filename, file=log_file)
        f.close()
    elif len(argv) == 3:
        image1 = loadImage(argv[1])
        hash1 = DifferenceHash(image1)
        print("\n" + argv[1] + "\t%(hash)016x" % {"hash": hash1})
        image2 = loadImage(argv[2])
        hash2 = DifferenceHash(image2)
        similarity = ((64 - bin(hash1 ^ hash2).count("1")) * 100.0) / 64.0
        print("Images are in", similarity, "% similar.")
# Executing file using:
#         argv[0]     argv[1]             argv[2]        argv[3]                     argv[4]
# python3 szperacz.py <pattern_list_paths> <search_path> <txt_file_with_changes_log> <%>
    elif len(argv) == 5:
        x = 0
        for i in argv:
            print(str(x) + ": " + i)
            x += 1
        log_file = open(argv[3], 'a')
        image1 = loadImage(argv[1])
        hash1 = DifferenceHash(image1)
        print("\n" + argv[1] + "\t%(hash)016x" % {"hash": hash1})
        for filename in glob.iglob(argv[2].rstrip('/')+'/**/*.*', recursive=True):
            if isImage(filename):
                try:
                    image2 = loadImage(filename)
                except:
                    nf = open('error_log.txt', 'a')
                    nf.write("ERROR with file: " + filename + "\n")
                    continue
                hash2 = DifferenceHash(image2)
                similarity = ((64 - bin(hash1 ^ hash2).count("1")) * 100.0) / 64.0
                if similarity >= float(argv[4]):
                    print("\n" + filename + " " + str(similarity) + "\t%(hash)016x" % {"hash": hash2})
                    print(str(similarity) + "\t" + filename, file=log_file)
    elif argv[1] == "--help":
        print("\n"
              "Poprawne wywołania skryptu:\n"
              "  1 - porównanie dwóch obrazków\n"
              "\t Sposób użycia:\n"
              "\t python3 szperacz.py <img1> <img2>\n"
              "  2 - przeszukanie dogłebne podaniej ścieżki w poszukiwaniu doplikatów, podmianie ich i wypisaniu ich w logach\n"
              "\t Sposób użycia:\n"
              "\t python szperacz.py <wzór_do_porównania> <obrazek_do_podmiany> <ścieżka_przeszukiwania> <plik_do_logów> <minimalny_%_porównania>\n"
              "\t Przykład: python3 szperacz.py wzór.jpg nowy.png /media/user.dzp-c.ap.lan/ log_file.txt 91\n"
              "  3 - przeszukanie dogłebne podaniej ścieżki w celu znalezienia u wypisania duplikatów\n"
              "\t Sposób użycia:\n"
              "\t python3 poszukiwacz.py <wzór_do_porównania> <ścieżka_przeszukiwania> <plik_do_logów> <minimalny_%_podobieństwa>\n"
              "\t Przykład: python3 szperacz.py wzór.jpg /media/user.dzp-c.ap.lan/ log_file.txt 80\n"
              "")
    else:
        print("\n aby uzyskać pomoc wywołaj skrypt z argumentem '--help'\n")