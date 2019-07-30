import data
import normaldistribution


def main():

    """
    Demonstrate the NormalDistribution class with a dataset
    created using the data module.
    """

    print("-----------------------")
    print("| codedrome.com       |")
    print("| Normal Distribution |")
    print("-----------------------\n")

    d = data.generate_data()

    nd = normaldistribution.NormalDistribution()

    nd.data = d

    nd.calculate_prob_dist()

    nd.print_prob_dist()


main()
