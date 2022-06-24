import pandas as pd
from argh import dispatch_command


def main(metadata: str) -> None:
    dates = ['2020-06-01',
             '2021-01-01',
             '2021-06-01',
             '2022-01-01']
    df = pd.read_csv(metadata, sep='\t')
    df = df[df["country"]=="Belgium"]

    print(df.columns)
    provinces = set()
    for p in df["division"]:
        provinces.add(p)

    print(sorted(list(provinces)))
    provinces = ["Antwerpen",
                 "BrabantWallon",
                 "Brussels",
                 "Hainaut",
                 "Limburg",
                 "Liège",
                 "Luxembourg",
                 "Namur",
                 "OostVlaanderen",
                 "VlaamsBrabant",
                 "WestVlaanderen"]

    with open("data/sequence_counts.tsv", "w") as f:
        header = "province\t" + "\t".join(dates) + "\n"
        f.write(header)
        for province in provinces:
            line = province
            for date in dates:
                seqs = len(df[df["division"]==province][df["date"]<=date])
                line += f"\t{seqs}"
            line += "\n"
            f.write(line)


if __name__=="__main__":
    dispatch_command(main)
