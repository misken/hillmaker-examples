

import pandas as pd
import hillmaker as hm

file_stopdata = '../data/ShortStay.csv'

# Required inputs
scenario = 'sstest_60'
in_fld_name = 'InRoomTS'
out_fld_name = 'OutRoomTS'
cat_fld_name = 'PatType'
start = '1/1/1996'
end = '3/30/1996 23:45'

# Optional inputs
bin_mins = 120
output_path = './output'


df = pd.read_csv(file_stopdata, parse_dates=[in_fld_name, out_fld_name])

hm.make_hills(scenario, df, in_fld_name, out_fld_name,
                     start, end, cat_fld_name,
                     tot_fld_name, bin_mins,
                     export_path=output_path,
                     verbose=1)
