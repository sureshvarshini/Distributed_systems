import argparse
from introduction import introduce

if __name__ =="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--shop', type=str)
    parser.add_argument('--region', type=str)
    parser.add_argument('--id', type=str)
    parser.add_argument('--delay', type=str)
    args = parser.parse_args()
    
    introduce(args.shop,args.region,args.delay)

    print("Checking points balnce for you...")