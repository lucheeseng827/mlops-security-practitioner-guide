import glob
import pandas as pd
import tarfile
import urllib.request
from kfp.v2 import dsl
    
def download_and_merge_csv(url: str, output_csv: str):
  with urllib.request.urlopen(url) as res:
    tarfile.open(fileobj=res, mode="r|gz").extractall('data')
  df = pd.concat(
      [pd.read_csv(csv_file, header=None) 
       for csv_file in glob.glob('data/*.csv')])
  df.to_csv(output_csv, index=False, header=False)

# Define a pipeline and create a task from a component:
@dsl.pipeline(
    name='my-pipeline',
    # You can optionally specify your own pipeline_root
    # pipeline_root='gs://my-pipeline-root/example-pipeline',
)
def my_pipeline(url: str):
  web_downloader_task = web_downloader_op(url=url)
  merge_csv_task = merge_csv(tar_data=web_downloader_task.outputs['data'])
  # The outputs of the merge_csv_task can be referenced using the
  # merge_csv_task.outputs dictionary: merge_csv_task.outputs['output_csv']

download_and_merge_csv(
    url='https://storage.googleapis.com/ml-pipeline-playground/iris-csv-files.tar.gz', 
    output_csv='merged_data.csv')

