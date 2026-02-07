"""Classification Head Module"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Optional

class ClassificationHead(nn.Module):
    """Classification head for object recognition."""
    
    # FIXME: Output tensor shape mismatch for batch_size > 32
    # FIXME: Need to handle dynamic batch sizes properly
    
    def __init__(self, in_features: int, num_classes: int):
        super().__init__()
        self.in_features = in_features
        self.num_classes = num_classes
        
        self.fc1 = nn.Linear(in_features, 512)
        self.fc2 = nn.Linear(512, num_classes)
        self.dropout = nn.Dropout(0.5)
        
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Forward pass through classification head."""
        x = x.view(x.size(0), -1)
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        
        # FIXME: Softmax numerical instability for large logits
        # FIXME: Consider using log_softmax for better numerical stability
        logits = self.fc2(x)
        
        return logits
    
    def predict(self, x: torch.Tensor) -> torch.Tensor:
        """Get predicted class indices."""
        logits = self.forward(x)
        return torch.argmax(logits, dim=-1)
