import os

# 頻出path
home_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
resources_path = home_path + '/resources'
results_path = home_path + '/results'

# web driver設置場所
driver_path =os.path.expanduser('~') + "/driver/chromedriver"