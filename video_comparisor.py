import subprocess

if __name__ == "__main__":

    # compare vp8 and vp9 codecs using blend filters
    # (https://ffmpeg.org/ffmpeg-filters.html#blend-1)
    # https://stackoverflow.com/questions/25774996/how-to-compare-show-the-
    # difference-between-2-videos-in-ffmpeg

    subprocess.call(["ffmpeg", "-i", "BBB_720_vp8.webm", "-i",
                     "BBB_720_vp9.webm", "-filter_complex",
                     "blend=all_mode=difference", "-c:v",
                     "libx264", "-crf", "18", "-c:a", "copy",
                     "vp8_vp9_comparison.mkv"])

    # compare the same codecs but with a lower resolution
    subprocess.call(["ffmpeg", "-i", "BBB_120_vp8.webm", "-i",
                     "BBB_120_vp9.webm", "-filter_complex",
                     "blend=all_mode=difference", "-c:v",
                     "libx264", "-crf", "18", "-c:a", "copy",
                     "vp8_vp9_comparison_lr.mkv"])

    # We can observe that the difference between both codecs is almost
    # unnoticeable. This lies on the objects, such as trees, which are
    # slightly different in the codecs.
    # An interesting observation is that with a lower resolution the difference
    # is even lower, although with the letters of the title there are more blurred,
    # meaning that the difference is greater.
