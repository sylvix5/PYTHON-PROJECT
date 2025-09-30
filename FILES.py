import sys
import pandas as pd

def main():
    df = pd.read_csv('FAOSTAT_data_7-23-2022.csv')
    # Filter Ghana
    ghana_df = df[(df["Area"] == "Ghana") & (df["Item"] == "Cocoa, beans")]

    # Filter Côte d'Ivoire
    civ_df = df[(df["Area"] == "Côte d'Ivoire") & (df["Item"] == "Cocoa, beans")]

    # Save as new CSV files in your project folder
    ghana_df.to_csv("ghana_cocoa.csv", index=False)
    civ_df.to_csv("civ_cocoa.csv", index=False)

    print("✅ Files saved: ghana_cocoa.csv and civ_cocoa.csv")


    return 0


if __name__ == "__main__":
    sys.exit(main())