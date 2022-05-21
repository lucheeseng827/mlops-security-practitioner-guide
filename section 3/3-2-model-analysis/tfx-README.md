
###TFX guide
# reference: https://colab.research.google.com/github/tensorflow/tfx/blob/master/docs/tutorials/tfx/template.ipynb#scrollTo=Hw3nsooU0okv


# run these in your local/remote IDE
import sys
# Use the latest version of pip.
!pip install --upgrade pip
# Install tfx and kfp Python packages.
!pip install --upgrade "tfx[kfp]<2"


# check on the version of tfx
python3 -c "from tfx import version ; print('TFX version: {}'.format(version.__version__))"

python -c "from tfx import version ; print('TFX version: {}'.format(version.__version__))"


# shell_output=!gcloud config list --format 'value(core.project)' 2>/dev/null
GOOGLE_CLOUD_PROJECT=shell_output[0]
%env GOOGLE_CLOUD_PROJECT={GOOGLE_CLOUD_PROJECT}
print("GCP project ID:" + GOOGLE_CLOUD_PROJECT)


# endpoint example(note without https://): 1e9deb537390ca22-dot-asia-east1.pipelines.googleusercontent.com 


# This refers to the KFP cluster endpoint
ENDPOINT='' # Enter your ENDPOINT here.
if not ENDPOINT:
    from absl import logging
    logging.error('Set your ENDPOINT in this cell.')


# declaring tfx image path
CUSTOM_TFX_IMAGE='gcr.io/' + GOOGLE_CLOUD_PROJECT + '/tfx-pipeline'