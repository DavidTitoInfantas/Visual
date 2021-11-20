# sweetviz public interface
# -----------------------------------------------------------------------------------
__title__ = 'sweetviz_drz'
__version__ = "2.1.3"
__author__ = "Francois Bertrand"
__license__ = 'MIT'

# These are the main API functions
from sweetviz_drz.sv_public import analyze, compare, compare_intra
from sweetviz_drz.feature_config import FeatureConfig

# This is the main report class; holds the report data
# and is used to output the final report
from sweetviz_drz.dataframe_report import DataframeReport

# This is the config_parser, use to customize settings
from sweetviz_drz.config import config as config_parser
