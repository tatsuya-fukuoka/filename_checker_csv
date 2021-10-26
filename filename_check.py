import glob
def main():
    files = glob.glob("*.csv")
    for file in files:
        print(file)

if __name__ == '__main__':
    main()
