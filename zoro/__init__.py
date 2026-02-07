"""
ZORO - Zero-shot Object Recognition Operations
A Computer Vision Framework
"""

__version__ = "0.1.0"

# TODO: Add lazy imports for heavy modules
# TODO: Set up logging configuration
# TODO: Add version compatibility checks

from .core import detector, segmentation
from .models import backbone
from .training import trainer
from .evaluation import metrics
from .utils import preprocessing
