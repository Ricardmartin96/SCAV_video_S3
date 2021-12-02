import subprocess

if __name__ == "__main__":

# https://trac.ffmpeg.org/wiki/StreamingGuide
    # ffmpeg -i Big_Buck_Bunny.mp4 -preset ultrafast -vcodec libx264 -tune
    # zerolatency -b 900k -f mpegts udp://10.80.130.199

    ip = input("Inserta una IP: ")
    ip = "udp://"+ip+"/5000"

    # Retransmetem un video en la ip anterior
    subprocess.call(["ffmpeg", "-i", "Big_Buck_Bunny.mp4", "-preset",
                     "ultrafast", "-vcodec", "libx264", "-tune", "zerolatency",
                     "-b", "900k", "-f", "mpegts", ip])

# https://es.brickcom.com/support/faq_contents.php?id=7
    # open link in VLC: App - Medio - Abrir ubicacion de red
    # udp://127.0.0.1:5000