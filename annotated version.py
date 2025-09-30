import sys
import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Load data
    ghana = pd.read_csv("ghana_cocoa.csv")
    civ = pd.read_csv("civ_cocoa.csv")

    # Prepare subsets
    ghana_yield = ghana[ghana["Element"] == "Yield"].sort_values("Year")
    civ_yield = civ[civ["Element"] == "Yield"].sort_values("Year")
    ghana_harvest = ghana[ghana["Element"] == "Area harvested"].sort_values("Year")
    civ_harvest = civ[civ["Element"] == "Area harvested"].sort_values("Year")

    # Create 2x2 grid of subplots
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))

    # Ghana Yield (scatter)
    axs[0, 0].scatter(ghana_yield["Year"], ghana_yield["Value"], color="purple")
    axs[0, 0].set_title("Ghana Cocoa Yield")
    axs[0, 0].set_xlabel("Year")
    axs[0, 0].set_ylabel(f"Yield ({ghana_yield['Unit'].iloc[0]})")

    # Côte d'Ivoire Yield (scatter)
    axs[0, 1].scatter(civ_yield["Year"], civ_yield["Value"], color="red")
    axs[0, 1].set_title("Côte d'Ivoire Cocoa Yield")
    axs[0, 1].set_xlabel("Year")
    axs[0, 1].set_ylabel(f"Yield ({civ_yield['Unit'].iloc[0]})")

    # Ghana Harvested (bar)
    axs[1, 0].bar(ghana_harvest["Year"], ghana_harvest["Value"], color="green")
    axs[1, 0].set_title("Ghana Area Harvested")
    axs[1, 0].set_xlabel("Year")
    axs[1, 0].set_ylabel(f"Area Harvested ({ghana_harvest['Unit'].iloc[0]})")

    # Côte d'Ivoire Harvested (bar)
    axs[1, 1].bar(civ_harvest["Year"], civ_harvest["Value"], color="orange")
    axs[1, 1].set_title("Côte d'Ivoire Area Harvested")
    axs[1, 1].set_xlabel("Year")
    axs[1, 1].set_ylabel(f"Area Harvested ({civ_harvest['Unit'].iloc[0]})")

    # Add overall title
    fig.suptitle("Cocoa Production: Ghana vs Côte d'Ivoire", fontsize=16, fontweight="bold")

    # Adjust layout (leave room for main title)
    plt.tight_layout(rect=[0, 0, 1, 0.96])

    # Save as PDF
    plt.savefig("cocoa_analysis.pdf")

    # Show plot
    plt.show()

    return 0

if __name__ == "__main__":
    sys.exit(main())
