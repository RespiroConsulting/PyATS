import json
import requests

def main():
    f = open("out.txt").read()
    print("""This test is performed to identify the changes in BGP network include,
             1. Number of network entries
             2. Number of BGP neighbors
             3. BGP neighbors status
             4. Number of BGP routes""")
    if f == "":
        print('\n'+"No changes found in BGP network before and after interface change"+'\n')
        simplefile = open("doc1.txt").read()
        print(simplefile)
        print("Please find the attached file(s) for more detailed output of each command.")
    else:
        print('\n'+"Observed changes in BGP settings before and after interface change:"+'\n' +f)
        print("Please find the attached file(s) for more detailed output of each command.")
if __name__ == '__main__':
    main()
