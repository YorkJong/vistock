Change Log
==========
TODO
----

0.3.3
------------------
* vistock/util.py: Added the support of .TWO to decide_market_color_style
* vistock/util.py: Added doctest to decide_market_color_style
* vistock/mpl/rsi.py: Created ta module and replaced talib package with ta
  module

0.3.2 [2024-07-22]
------------------
* vistock/mpl: Added market_color_style argument to stock plot functions
* vistock/plotly: Added market_color_style argument to stock plot functions

0.3.1 [2024-07-21]
------------------
* Added the support of bull-run and drawdown stock chart (mplfinance version)
* Added the support of bull-run and drawdown stock chart (Plotly version)

0.3.0 [2024-07-19]
------------------
* Added Turnover Profile feature
* Made both price axes have the same scale and range (Plotly version)
* Added 'hbar_align_on_right' parameter pbv2s.plot function to allow the
  starting position of the horizontal bars on the right.

0.2.5 [2023-02-20]
------------------
* Renamed parameter 'ticker' to 'symbol'
* Renamed folder 'examples' to 'notebooks'
* Added chinese stock name support for Taiwan stocks
* Applied __file__ to generate output filenames
* Added parameter "out_dir" to plot functions

0.2.4 [2023-02-14]
------------------
* vistock.plotly: Added "hides_nontrading" parameter to plot functions
* vistock_demo.ipynb: Added "hides_nontrading" parameter to Plotly forms
* Added files for sphinx document generator

0.2.3 [2023-02-13]
------------------
* vistock_demo.ipynb: Fixed "NameError: name 'sys' is not defined
* vistock_demo.ipynb: Added "total_bins" parameter to the "mplfinance:interval
  of intraday" form.
* vistock_demo.ipynb: Added Explanation cells to explain parameters and forms

0.2.2 [2023-02-13]
------------------
* Fixed remove_nontrading issue on interval < 1day
* Added "total_bins" parameter to forms on vistock_demo.ipynb

0.2.1 [2023-02-11]
------------------
* Added the version number to 0.2.1
* Filled README.md
* Appled 4 Colab Forms to vistock_demo.ipynb for demo
* Added "interval" parameter for all plot functions
* Refined output filenames for all plot functions
* Fine tuned the legend location for all plotly plot functions
* Refined titles and output finename
* Added test_mpl.py
* Renamed test_on_plotly.py to test_plotly.py
* Fine tuned colors

0.2.0 [2023-02-09]
------------------
* Add vistock_demo.ipynb
* Add test_on_ploly.py
* Add hovermode dropdown menu

0.1 [2023-02-07]
----------------
* Initial version
* Extracted from ViStock.ipynb
