import argparse
import zlib
import sys

def Zlib():
    parser = argparse.ArgumentParser(description="A command-line tool for using the zlib compression algorithm.")
    parser.add_argument("-d", "--decompress", action="store_true", help="Decompresses the input instead of compressing the output.")
    args = parser.parse_args()

    if args.decompress:
        decompressor = zlib.decompressobj()
        try:
            while True:
                chunk = sys.stdin.buffer.read(1024)
                if not chunk:
                    break
                sys.stdout.buffer.write(decompressor.decompress(chunk))
        except Exception as e:
            exit(str(e), 1)
    else:
        compressor = zlib.compressobj()
        try:
            while True:
                chunk = sys.stdin.buffer.read(1024)
                if not chunk:
                    break
                sys.stdout.buffer.write(compressor.compress(chunk))
            sys.stdout.buffer.write(compressor.flush())
        except Exception as e:
            exit(str(e), 1)

def exit(msg, code):
    print(msg)
    sys.exit(code)

if __name__ == "__main__":
    Zlib()
    # test


# Examples
# Compress : zlib < file > file.zlib
# decompress : zlib -d < file.zlib
# Compressing and base64-encoding some json  echo -n '{"foo":"bar"}' | zlib | base64
# Decoding and decompressing some base64-encoded and zlib-compressed input echo -n 'eJyqVkrLz1eyUkpKLFKqBQQAAP//HXoENA==' | base64 -D | zlib -d