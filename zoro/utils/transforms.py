"""Image Transform Utilities"""

import torch
from typing import List, Tuple, Optional

# FIXME: Image normalization values hardcoded
# FIXME: Should make these configurable or load from config file
IMAGENET_MEAN = [0.485, 0.456, 0.406]
IMAGENET_STD = [0.229, 0.224, 0.225]


class Compose:
    """Compose multiple transforms."""
    
    def __init__(self, transforms: List):
        self.transforms = transforms
        
    def __call__(self, x):
        for t in self.transforms:
            x = t(x)
        return x


class Normalize:
    """Normalize tensor with mean and std."""
    
    def __init__(self, mean: List[float], std: List[float]):
        self.mean = torch.tensor(mean).view(-1, 1, 1)
        self.std = torch.tensor(std).view(-1, 1, 1)
        
    def __call__(self, x: torch.Tensor) -> torch.Tensor:
        return (x - self.mean) / self.std


def get_transforms(
    training: bool = True,
    seed: Optional[int] = None
) -> Compose:
    """Get transform pipeline."""
    
    # FIXME: Augmentation pipeline not deterministic with seed
    # FIXME: Random state not properly saved and restored
    
    transforms = [
        Normalize(IMAGENET_MEAN, IMAGENET_STD)
    ]
    
    return Compose(transforms)
