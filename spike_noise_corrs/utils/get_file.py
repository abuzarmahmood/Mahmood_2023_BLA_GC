import tables
import os
from glob import glob
import pandas as pd
from tqdm import tqdm

dir_name = '/media/fastdata/Thomas_Data/data/TG22/TG22Day1Exp1_230619_135531'
basename = os.path.basename(dir_name)
h5_files = glob(os.path.join(dir_name, '*.h5'))

# h5 = tables.open_file(h5_files[0], 'r')
# h5.close()
h5_base_path = '/ancillary_analysis/spike_noise_corrs'
df_names = [
        'inter_region',
        'intra_region',
        'shuffle_inter_region',
        'shuffle_intra_region',
        ]

dfs = {}
for name in tqdm(df_names):
    fin_name = name+'_frame'
    path = os.path.join(h5_base_path, fin_name)
    this_df = pd.read_hdf(h5_files[0], path)
    mean_df = this_df.groupby(['pair_ind','taste']).mean()
    mean_df = mean_df.reset_index()
    mean_df['corr_type'] = name
    dfs[name] = mean_df

cat_df = pd.concat(dfs.values())

out_dir = os.path.join(dir_name, 'artifacts','spike_noise_corrs')
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, f'{basename}_spike_noise_corrs.pkl') 
cat_df.to_pickle(out_path)
# for name, df in dfs.items():
#     out_path = os.path.join(out_dir, name+'.pkl')
#     df.to_pickle(out_path)
#     print(f'Saved {name} to {out_path}')
