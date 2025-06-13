import matplotlib.pyplot as plt

relative_google_searche_for_sleep_walking = [  36, 70, 77, 76, 57, 52, 45, 40, 36, 37]
backelor_degrees_awarded_in_law_enforcement = [ 54, 60, 62, 62.8, 61, 59.5, 58, 57.3, 57, 57.9] # In thousands
years = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]

def main():
    plt.plot(years, relative_google_searche_for_sleep_walking, label='Google Searches for Sleep Walking')
    plt.plot(years, backelor_degrees_awarded_in_law_enforcement, label='Bachelor Degrees in Law Enforcement')
    plt.title('Sleep Walking Searches vs Law Enforcement Degrees')
    plt.xlabel('Year')
    plt.ylabel('Relative Search Volume / Degrees Awarded (in Thousands)')
    plt.legend()
    plt.savefig("expected_plot.png")
    


if __name__ == "__main__":
    main()