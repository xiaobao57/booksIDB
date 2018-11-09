import pandas as pd

def main():

    df = pd.read_json('books.json')
    print(df['publishers'][86][0]['name'])
    print(df['publishers'][86][0]['parent company'])

main()
