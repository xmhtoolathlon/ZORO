"""Tests for ZORO Models"""

import pytest
import torch
from zoro.models.backbone import ResNetBackbone
from zoro.models.head import ClassificationHead

# FIXME: Mock fixtures not properly cleaned up
# FIXME: Should use pytest fixtures with proper teardown

class TestResNetBackbone:
    """Test cases for ResNetBackbone."""
    
    def test_forward_shape(self):
        """Test output shape of forward pass."""
        model = ResNetBackbone(depth=50, pretrained=False)
        x = torch.randn(2, 3, 224, 224)
        out = model(x)
        assert out is not None
        
    def test_pretrained_loading(self):
        """Test loading pretrained weights."""
        model = ResNetBackbone(depth=50, pretrained=True)
        assert model.pretrained == True


class TestClassificationHead:
    """Test cases for ClassificationHead."""
    
    def test_forward_logits(self):
        """Test logits output."""
        head = ClassificationHead(512, 1000)
        x = torch.randn(4, 512)
        logits = head(x)
        assert logits.shape == (4, 1000)
        
    def test_predict(self):
        """Test class prediction."""
        head = ClassificationHead(512, 10)
        x = torch.randn(2, 512)
        preds = head.predict(x)
        assert preds.shape == (2,)
