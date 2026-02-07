# ZORO - Zero-shot Object Recognition and Optimization

> 🔬 **Feature Branch** - Development branch for ZORO framework improvements

## About ZORO

ZORO is a cutting-edge framework for zero-shot object recognition using advanced neural network architectures. This repository contains experimental features under development.

## 🔧 Development Status

This feature branch contains active development with several known issues that need attention.

## 🚀 Quick Start

```bash
# Clone the repository
git clone <repository-url>
cd ZORO

# Install dependencies
pip install -r requirements.txt

# Note: Check known issues below before running
```

## 📁 Project Structure

```
ZORO/
├── zoro/                    # Core framework
│   ├── models/              # Neural network models
│   ├── utils/               # Utility functions
│   └── inference/           # Inference engine
├── tests/                   # Test suite
└── README.md               # This file
```

## ⚠️ Development Notes

- This is an **experimental feature branch**
- Several components have known issues marked with FIXME
- Memory optimization and GPU handling need attention


### 🔴 High Priority Issues

- **Memory Management**: GPU memory leaks in inference pipeline
- **Model Loading**: Checkpoint compatibility issues
- **Data Pipeline**: Batch processing inefficiencies
- **Logging**: Inconsistent log formatting across modules

### 🐛 Known Issues List

- [ ] **zoro/models/backbone.py:23** - Memory leak when loading large models
- [ ] **zoro/models/backbone.py:45** - Deprecated torch.cuda.amp usage needs migration
- [ ] **zoro/models/backbone.py:67** - Gradient checkpointing not working for all layers
- [ ] **zoro/models/head.py:15** - Output tensor shape mismatch for batch_size > 32
- [ ] **zoro/models/head.py:38** - Softmax numerical instability for large logits
- [ ] **zoro/utils/data_loader.py:12** - Memory not released after dataloader iteration
- [ ] **zoro/utils/data_loader.py:34** - Prefetch queue grows unbounded
- [ ] **zoro/utils/data_loader.py:56** - Worker processes not properly terminated
- [ ] **zoro/utils/transforms.py:19** - Image normalization values hardcoded
- [ ] **zoro/utils/transforms.py:41** - Augmentation pipeline not deterministic with seed
- [ ] **zoro/inference/engine.py:28** - CUDA stream synchronization missing
- [ ] **zoro/inference/engine.py:52** - Model warm-up not implemented
- [ ] **zoro/inference/engine.py:78** - Batch inference timeout not configurable
- [ ] **tests/test_models.py:16** - Mock fixtures not properly cleaned up
- [ ] **tests/test_utils.py:22** - Temporary files not deleted after tests

## 🤝 Contributing

1. Pick a FIXME item from the issues list above
2. Fix the issue and add tests
3. Update this README when issues are resolved
