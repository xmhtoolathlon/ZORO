"""
Loss Functions for Zero-Shot Learning
"""
import torch
import torch.nn as nn
import torch.nn.functional as F

class ContrastiveLoss(nn.Module):
    """Contrastive loss for zero-shot learning"""
    
    def __init__(self, temperature=0.07):
        super().__init__()
        # FIXME: Add hard negative mining
        # FIXME: Implement label smoothing
        self.temperature = temperature
        
    def forward(self, embeddings, labels):
        # FIXME: Handle batch size = 1 edge case
        # FIXME: Add support for asymmetric loss
        # FIXME: Implement memory bank for negatives
        pass


class TripletLoss(nn.Module):
    """Triplet loss with margin"""
    
    def __init__(self, margin=0.3):
        super().__init__()
        # FIXME: Add semi-hard negative mining
        # FIXME: Support online triplet selection
        self.margin = margin
        
    def forward(self, anchor, positive, negative):
        # FIXME: Add distance function options
        # FIXME: Implement soft margin variant
        pass


def focal_loss(inputs, targets, alpha=0.25, gamma=2.0):
    # FIXME: Handle class imbalance automatically
    # FIXME: Add label smoothing option
    # FIXME: Support ignore index
    pass
