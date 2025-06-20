from plot_helpers import make_bar_chart, make_scatter_plot
from data_loaders import load_fruit_dict, load_study_data_df

def main():
    fruit = load_fruit_dict()
    make_bar_chart(fruit, "fruit", "counts", "fruit.jpg")

    study_data = load_study_data_df()
    make_scatter_plot(study_data['Hours Studied'].to_list(), 
                      study_data['Exam Score'].to_list(), 
                      'Hours Studied', 
                      'Exam Score', 
                      "study_data.jpg")
    

if __name__ == "__main__":
    main()