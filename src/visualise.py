import sys
from visualisations.geo import draw_gauteng, rename_for_ffmpeg

height=float(sys.argv[1])
width=int(sys.argv[2])
size=int(sys.argv[3])
scaling_factor=float(sys.argv[4])
n_jobs=int(sys.argv[5])
draw_gauteng(height, width, size, scaling_factor,n_jobs)
rename_for_ffmpeg('C:/Development/park-crawler/visualisations/output/gauteng')

#python visualise.py 150000 150000 20 30 1
#ffmpeg -r 15 -i "C:\Development\park-crawler\visualisations\output\gauteng\%d.png" "C:\Development\park-crawler\visualisations\output\gauteng.mp4"