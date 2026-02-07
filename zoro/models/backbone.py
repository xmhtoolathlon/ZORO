"""Neural Network Backbone Models"""

import torch
import torch.nn as nn
from typing import Optional, List

class ResNetBackbone(nn.Module):
    """ResNet-based backbone for feature extraction."""
    
    def __init__(self, depth: int = 50, pretrained: bool = True):
        super().__init__()
        self.depth = depth
        self.pretrained = pretrained
        
        # FIXME: Memory leak when loading large models - need to clear cache after load
        # FIXME: Consider using memory-mapped loading for very large checkpoints
        self.layers = self._build_layers()
        
    def _build_layers(self) -> nn.ModuleList:
        """Build the backbone layers."""
        layers = nn.ModuleList()
        
        # Initial convolution
        layers.append(nn.Conv2d(3, 64, kernel_size=7, stride=2, padding=3))
        layers.append(nn.BatchNorm2d(64))
        layers.append(nn.ReLU(inplace=True))
        
        # FIXME: Deprecated torch.cuda.amp usage needs migration to new API
        # FIXME: The autocast context manager should use torch.amp.autocast
        
        return layers
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Forward pass through backbone."""
        for layer in self.layers:
            x = layer(x)
        
        # FIXME: Gradient checkpointing not working for all layers
        # FIXME: Need to investigate checkpoint_sequential compatibility
        
        return x
    
    def load_pretrained(self, checkpoint_path: str) -> None:
        """Load pretrained weights."""
        # FIXME: Checkpoint compatibility issues between versions
        checkpoint = torch.load(checkpoint_path)
        self.load_state_dict(checkpoint, strict=False)
