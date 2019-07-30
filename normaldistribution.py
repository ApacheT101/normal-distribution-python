import math


class NormalDistribution(object):

    """
    Has list attributes for data and the data's probability distribution, which
    is calculated by calling the calculate_prob_dist method. Also attributes for totals.
    """

    def __init__(self):

        """
        Create attributes with default values.
        """

        self.data = []
        self.probability_distribution = []

        self.total_frequency = 0
        self.total_probability = 0.0
        self.total_normal_probability = 0.0
        self.total_normal_frequency = 0.0

    def calculate_prob_dist(self):

        """
        Iterate the data, adding dictionary to probability distribution list for new values
        or incrementing frequencies of existing ones.
        Then calculates actual probabilities, and normal probabilities and frequencies.
        """

        self.total_frequency = len(self.data)

        data_total = 0
        sum_of_squares = 0

        for item in self.data:

            # try to find current value in probability distribution list
            index = self.__index_of(item, self.probability_distribution)

            if index < 0:

                # if not present add to list
                self.probability_distribution.append({"value": item, "frequency": 1, "probability": 0, "normal_probability": 0, "normal_frequency": 0})

            else:

                # if present increment frequency
                self.probability_distribution[index]["frequency"] += 1

            data_total += item
            sum_of_squares += (item ** 2)

        # calculate mean, variance and standard deviation
        mean = data_total / self.total_frequency
        variance = (sum_of_squares - ((data_total ** 2) / self.total_frequency)) / self.total_frequency
        stddev = variance ** 0.5

        # calculate probabilities of each unique value
        for pd in self.probability_distribution:

            pd["probability"] = pd["frequency"] / len(self.data)

            pd["normal_probability"] = ((1.0 / (stddev * math.sqrt(2.0 * math.pi))) * (pow(math.e, -1.0 * ((pow((pd["value"] - mean), 2.0)) / ( variance * 2.0)))))

            pd["normal_frequency"] = pd["normal_probability"] * len(self.data)

            self.total_probability += pd["probability"]
            self.total_normal_probability += pd["normal_probability"]
            self.total_normal_frequency += pd["normal_frequency"]

        self.probability_distribution.sort(key = lambda k: k['value'])

    def print_prob_dist(self):

        """
        Print details of each item in the probability distribution and totals.
        """

        print("Value | Probability | Normal Prob | Freq | Normal Freq\n------------------------------------------------------");

        for item in self.probability_distribution:

            print("{:5d} |{:12.4f} |{:12.4f} |{:5d} |{:12.4f}".format(item["value"], item["probability"], item["normal_probability"], item["frequency"], item["normal_frequency"]))

        print("------------------------------------------------------")

        print("      |{:12.4f} |{:12.6f} |{:5.0f} |{:12.4f}".format(self.total_probability, self.total_normal_probability, self.total_frequency, self.total_normal_frequency))

        print("------------------------------------------------------")

    def __index_of(self, n, probdist):

        """
        Return index of n if already in probdist, or -1 if not.
        """

        for i in range(0, len(probdist)):

            if probdist[i]["value"] == n:

                return i

        return -1
