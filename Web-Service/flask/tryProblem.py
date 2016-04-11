from collections import Counter

def main():
    with open('cron') as text:
        collection = Counter(text.read())
    print [char for char, times in collection.items() if times<3]

if__name=='__main__':
    main()
