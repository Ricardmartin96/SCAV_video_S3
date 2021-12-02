import subprocess

if __name__ == "__main__":

    # convert mp4 into vp8
    subprocess.call(["ffmpeg", "-i", "BBB_720.mp4", "-c:v",
                     "libvpx", "-crf", "30", "-b:v", "0", "-b:a", "128k",
                     "-c:a", "libopus", "BBB_720_vp8.webm"])

    subprocess.call(["ffmpeg", "-i", "BBB_480.mp4", "-c:v",
                     "libvpx", "-crf", "30", "-b:v", "0", "-b:a", "128k",
                     "-c:a", "libopus", "BBB_480_vp8.webm"])

    subprocess.call(["ffmpeg", "-i", "BBB_240.mp4", "-c:v",
                     "libvpx", "-crf", "30", "-b:v", "0", "-b:a", "128k",
                     "-c:a", "libopus", "BBB_240_vp8.webm"])

    subprocess.call(["ffmpeg", "-i", "BBB_120.mp4", "-c:v",
                     "libvpx", "-crf", "30", "-b:v", "0", "-b:a", "128k",
                     "-c:a", "libopus", "BBB_120_vp8.webm"])

    # convert mp4 into vp9
    subprocess.call(["ffmpeg", "-i", "BBB_720.mp4", "-c:v",
                     "libvpx-vp9", "-crf", "30", "-b:v", "0", "-b:a", "128k",
                     "-c:a", "libopus", "BBB_720_vp9.webm"])

    subprocess.call(["ffmpeg", "-i", "BBB_480.mp4", "-c:v",
                     "libvpx-vp9", "-crf", "30", "-b:v", "0", "-b:a", "128k",
                     "-c:a", "libopus", "BBB_480_vp9.webm"])

    subprocess.call(["ffmpeg", "-i", "BBB_240.mp4", "-c:v",
                     "libvpx-vp9", "-crf", "30", "-b:v", "0", "-b:a", "128k",
                     "-c:a", "libopus", "BBB_240_vp9.webm"])

    subprocess.call(["ffmpeg", "-i", "BBB_120.mp4", "-c:v",
                     "libvpx-vp9", "-crf", "30", "-b:v", "0", "-b:a", "128k",
                     "-c:a", "libopus", "BBB_120_vp9.webm"])

    # convert to h265
    subprocess.call(["ffmpeg", "-i", "BBB_720.mp4", "-c:v",
                     "libvpx265", "-vtag", "hvc1", "-c:a", "copy",
                     "BBB_720_h265.mp4"])

    subprocess.call(["ffmpeg", "-i", "BBB_480.mp4", "-c:v",
                     "libvpx265", "-vtag", "hvc1", "-c:a", "copy",
                     "BBB_480_h265.mp4"])

    subprocess.call(["ffmpeg", "-i", "BBB_240.mp4", "-c:v",
                     "libvpx265", "-vtag", "hvc1", "-c:a", "copy",
                     "BBB_240_h265.mp4"])

    subprocess.call(["ffmpeg", "-i", "BBB_120.mp4", "-c:v",
                     "libvpx265", "-vtag", "hvc1", "-c:a", "copy",
                     "BBB_120_h265.mp4"])

    # convert to av1
    subprocess.call(["ffmpeg", "-i", "BBB_720.mp4", "-c:v",
                     "libaom-av1", "-strict", "-2", "-crf", "30", "-b:v", "0",
                     "BBB_720_av1.mkv"])

    subprocess.call(["ffmpeg", "-i", "BBB_480.mp4", "-c:v",
                     "libaom-av1", "-strict", "-2", "-crf", "30", "-b:v", "0",
                     "BBB_480_av1.mkv"])

    subprocess.call(["ffmpeg", "-i", "BBB_240.mp4", "-c:v",
                     "libaom-av1", "-strict", "-2", "-crf", "30", "-b:v", "0",
                     "BBB_240_av1.mkv"])

    subprocess.call(["ffmpeg", "-i", "BBB_120.mp4", "-c:v",
                     "libaom-av1", "-strict", "-2", "-crf", "30", "-b:v", "0",
                     "BBB_120_av1.mkv"])