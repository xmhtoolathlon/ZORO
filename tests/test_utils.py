"""Tests for ZORO Utilities"""

import pytest
import torch
import tempfile
import os

from zoro.utils.transforms import Normalize, get_transforms

# FIXME: Temporary files not deleted after tests
# FIXME: Should use pytest tmp_path fixture instead

class TestNormalize:
    """Test cases for Normalize transform."""
    
    def test_normalize_values(self):
        """Test normalization computation."""
        norm = Normalize([0.5], [0.5])
        x = torch.ones(1, 1, 4, 4)
        out = norm(x)
        assert torch.allclose(out, torch.ones_like(out))
        
    def test_normalize_shape(self):
        """Test output shape preservation."""
        norm = Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        x = torch.randn(2, 3, 32, 32)
        out = norm(x)
        assert out.shape == x.shape


class TestTransformPipeline:
    """Test cases for transform pipeline."""
    
    def test_get_transforms_training(self):
        """Test training transforms."""
        transforms = get_transforms(training=True)
        assert transforms is not None
        
    def test_get_transforms_eval(self):
        """Test evaluation transforms."""
        transforms = get_transforms(training=False)
        assert transforms is not None
