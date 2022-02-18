import os
import glob
import chardet

source_dir = r'C:\USERS\USER1\Document\Source'

new_files_list = glob.glob(os.path.join(source_dir, '*.txt'))

for file in new_files_list:
    rawdata = open(file, "rb").read()
    result = chardet.detect(rawdata)
    charenc = result['encoding']

    if charenc == "UTF-16":
        base_file = os.path.basename(file)
        with open(file, "rb") as source:
            data = source.read().decode("utf-16")

        os.remove(os.path.join(source_dir, base_file))

        with open(os.path.join(source_dir, base_file), "wb") as dest:
            dest.write(data.encode("utf-8"))
