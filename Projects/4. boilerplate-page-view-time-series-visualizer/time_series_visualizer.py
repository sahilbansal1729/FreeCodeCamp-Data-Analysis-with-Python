import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv" , index_col = 'date')
df.index = pd.to_datetime(df.index)

# Clean data
df = df[((df['value'] > df['value'].quantile(0.025))&(df['value']<df['value'].quantile(0.975)))]


def draw_line_plot():
    # Draw line plot
    plt.clf()
    fig = plt.gcf()
    fig.set_size_inches(20,10)
    plt.plot(df.value , color = 'Red')
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel('Date')
    plt.ylabel('Page Views');

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_ = df.copy()
    df_['year'] = df.index.year
    df_['month'] = df.index.month_name()

    # Draw bar plot
    plt.clf()
    fig1 = plt.gcf()
    fig1.set_size_inches(20,15)
    sns.barplot(x = 'year' , y = 'value' , data = df_ , hue = 'month' , palette = "tab10" , ci = None )
    plt.legend(title = "Months" , labels = ['January' ,'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December'])
    plt.xlabel("Years")
    plt.ylabel("Average Page Views");

    # Save image and return fig (don't change this part)
    fig1.savefig('bar_plot.png')
    return fig1

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    '''
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    '''
    df_ = df.copy()
    df_['month'] = df_.index.strftime("%b")
    df_['year'] = df_.index.year

    # Draw box plots (using Seaborn)
    plt.clf()
    fig2 , ax = plt.subplots(1,2)
    fig2.set_size_inches(30,10)
    sns.boxplot(x = 'year' , y = 'value' , data = df_ , ax = ax[0]).set(title = "Year-wise Box Plot (Trend)" , xlabel = "Year" , ylabel
                                                                        = "Page Views")

    sns.boxplot(x = 'month' , y = 'value' , data = df_ , ax = ax[1] , order = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug","Sep", "Oct", "Nov", "Dec")).set(title = "Month-wise Box Plot (Seasonality)", xlabel = "Month" , ylabel = "Page Views");

    # Save image and return fig (don't change this part)
    fig2.savefig('box_plot.png')
    return fig2
