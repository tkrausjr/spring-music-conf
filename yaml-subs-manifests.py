_author__ = 'tkraus-m'

import yaml
import argparse

# Initiate the parser
parser = argparse.ArgumentParser()
# add long and short argument
parser.add_argument('--file', '-f')
parser.add_argument('--image', '-i')
# read arguments from the command line
args = parser.parse_args()

print("Supplied File Argument is = ", args.file)
print("Supplied Tag Argument is = ", args.image + "\n")

with open(args.file) as f:
    doc = yaml.load(f, Loader=yaml.FullLoader)

    print("The New image Value is . . ." + args.image )
    for key, value in doc.items():
        print(key + " : " + str(type(value)) + " = " + str(value))
        if type(value) is list:
            print(str(len(value)))

print("\n")
print("The Existing k8s yaml image Value is . . ." )
print(doc["spec"]["template"]["spec"]["containers"][0]["image"])

doc["spec"]["template"]["spec"]["containers"][0]["image"] = args.image

print("The New kubernetes manifest image: Value is . . ." )
print(doc["spec"]["template"]["spec"]["containers"][0]["image"])
print("\n")
with open(args.file, 'w') as n:
    yaml.dump(doc, n)
