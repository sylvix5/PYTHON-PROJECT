import sys
import pandas as pd
import matplotlib.pyplot as plt

def main():
    ghana = pd.read_csv("ghana_cocoa.csv")
    civ = pd.read_csv("civ_cocoa.csv")

    # Ghana scatter plot
    ghana_yield = ghana[ghana["Element"] == "Yield"].sort_values("Year")
    plt.scatter(ghana_yield["Year"], ghana_yield["Value"], color="purple")
    plt.title("Ghana Cocoa Yield")
    plt.xlabel("Year")
    plt.ylabel(f"Yield ({ghana_yield['Unit'].iloc[0]})")
    plt.show()

    # Cote d'Ivoire scatter plot
    civ_yield = civ[civ["Element"] == "Yield"].sort_values("Year")
    plt.scatter(civ_yield["Year"], civ_yield["Value"], color="red")
    plt.title("Civ Cocoa Yield")
    plt.xlabel("Year")
    plt.ylabel(f"Yield ({civ_yield['Unit'].iloc[0]})")
    plt.show()

    # Bar chart for ghana
    ghana_harvest = ghana[ghana["Element"] == "Area harvested"].sort_values("Year")
    plt.bar(ghana_harvest["Year"], ghana_harvest["Value"], color="green")
    plt.title("Ghana Area Harvested")
    plt.xlabel("Year")
    plt.ylabel(f"Area Harvested ({ghana_harvest['Unit'].iloc[0]})")
    plt.show()

    # Bar chart for Cote d'Ivoire
    civ_harvest = civ[civ["Element"] == "Area harvested"].sort_values("Year")
    plt.bar(civ_harvest["Year"], civ_harvest["Value"], color="green")
    plt.title("Côte d'Ivoire Cocoa Area Harvested")
    plt.xlabel("Year")
    plt.ylabel(f"Area Harvested ({civ_harvest['Unit'].iloc[0]})")
    plt.show()

    return 0

if __name__ == "__main__":
    sys.exit(main())
