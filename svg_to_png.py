import cairosvg
import os
import sys
import os.path
from os import path


def get_svg_files_from_directory():
    try:
        if not path.exists(input_directory_path):
            print("No directory {} exists".format(input_directory_path))
            sys.exit(0)

        files = os.listdir(input_directory_path)
        if not files:
            print("No files in input directory")
            sys.exit(0)

        svg_files = list(filter(lambda x: '.svg' in x, files))
        if not svg_files:
            print("There is no svg files in directory {}".format(input_directory_path))
            sys.exit(0)

        return svg_files

    except OSError as e:
        print("Something went wrong", e)
        sys.exit(0)


def convert_svg_to_png(svg_files):
    try:
        check_output_dir()
        for file in svg_files:
            file_name, extension = os.path.splitext(file)
            file_name = file_name + ".png"
            input_filename = input_directory_path + "/" + file
            output_filename = output_directory_path + "/" + file_name
            cairosvg.svg2png(url=input_filename, write_to=output_filename)

    except OSError as e:
        print("Something went wrong", e)
        sys.exit(0)


def check_output_dir():
    # Safe check for output dir, creates if not exists OUTPUT_DIR_NAME
    if not os.path.exists(output_directory_path):
        os.mkdir(output_directory_path)


if __name__ == "__main__":

    try:
        input_directory_path = sys.argv[1]
        output_directory_path = sys.argv[2]
        svg_files = get_svg_files_from_directory()
        convert_svg_to_png(svg_files)

    except IndexError:
        print("Please provide input directory path and output directory path")
