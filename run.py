import re
import glob

written_flag = 0;
flag = 0;

##config_loc = r"C_Cpp_ConfigurationProperties.js"
folder_string = r"C:\Users\Andrew\.vscode\extensions\ms-vscode.cpptools*\out\src\LanguageServer\\"
file_string = r"configurations.js"
config_loc = glob.glob(folder_string + file_string)[0]
##config_loc = glob.glob(r"C:\Users\Andrew\.vscode\extensions\ms-vscode.cpptools*\out\src\LanguageServer\C_Cpp_ConfigurationProperties.js")[0]

with open(config_loc, 'r+') as config:
    old = config.readlines()
    config.seek(0)

    for line in old:
        if '"name": "WSL"' in line:
            print("Already patched")
            written_flag = 1
            break

    if (not written_flag):
        for line in old:
            if '`' in line:
                flag ^= 1
            config.write(line)
            if flag:
                if '"configurations": [' in line:
                    with open('WSL.txt') as template:
                        for line2 in template:
                            line2 = re.sub(r'\${(.+?)}', '$\\{\g<1>\\}', line2)
                            config.write(line2)
                        config.write('\n')

        print("Written")

input()
