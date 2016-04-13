from collections import Counter

def main():
    with open('cron') as text:
        collection = Counter(text.read())
    print collection

if __name__ == '__main__':
    main()
