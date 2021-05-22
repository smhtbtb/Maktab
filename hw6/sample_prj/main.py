# from unittest import mock
## import sys
# import io
from sample_pkg.views import PeugeotView, CarView

## suppress_text = io.StringIO()
## sys.stdout = suppress_text

# with mock.patch('sys.stdout', new=io.StringIO) as std_out:
PeugeotView().show()
CarView().show()


## sys.stdout = sys.stdout
