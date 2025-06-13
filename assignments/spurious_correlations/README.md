# Spurious Correlations
There is this website, titled [spurious correlations](https://www.tylervigen.com/spurious-correlations), that shows how two seemingly unrelated variables can have a correlation. In this assignment we look at one specific example:
Bachelor's degrees in law enforcement vs google search volume for the term "sleep walking".

You can see the spurrious correlation graph [here](https://www.tylervigen.com/spurious/correlation/1532_bachelors-degrees-awarded-in-law-enforcement_correlates-with_google-searches-for-sleepwalking).

In the starter code we have provided you with 3 lists:
`relative_google_searche_for_sleep_walking` - a list of relative google search volumes for the term "sleep walking".
`backelor_degrees_awarded_in_law_enforcement` - a list of the number of bachelor's degrees awarded in law enforcement.
`years` - a list of years from 2012 to 2021.

Using years as the x-axis, plot both `relative_google_searche_for_sleep_walking` and `backelor_degrees_awarded_in_law_enforcement` on the same graph. 

Your final graph should look similar to the png labeled `expected_plot.png` in this folder.

Hint: If you want to display the "legend" of the plot, you can call `plt.legend()` after plotting both lines, but before `plt.show()`. The legend will automatically use the labels you provided.