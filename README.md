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

- [ ] **tests/test_models.py:8** - Mock fixtures not properly cleaned up
- [ ] **tests/test_models.py:9** - Should use pytest fixtures with proper teardown
- [ ] **tests/test_utils.py:10** - Temporary files not deleted after tests
- [ ] **tests/test_utils.py:11** - Should use pytest tmp_path fixture instead
- [ ] **zoro/inference/engine.py:21** - CUDA stream synchronization missing
- [ ] **zoro/inference/engine.py:22** - Need to properly sync streams for accurate timing
- [ ] **zoro/inference/engine.py:32** - Model warm-up not implemented
- [ ] **zoro/inference/engine.py:33** - Should run dummy inference to warm up CUDA kernels
- [ ] **zoro/inference/engine.py:40** - Batch inference timeout not configurable
- [ ] **zoro/inference/engine.py:41** - Should implement proper timeout handling
- [ ] **zoro/models/backbone.py:15** - Memory leak when loading large models - need to clear cache after load
- [ ] **zoro/models/backbone.py:16** - Consider using memory-mapped loading for very large checkpoints
- [ ] **zoro/models/backbone.py:28** - Deprecated torch.cuda.amp usage needs migration to new API
- [ ] **zoro/models/backbone.py:29** - The autocast context manager should use torch.amp.autocast
- [ ] **zoro/models/backbone.py:38** - Gradient checkpointing not working for all layers
- [ ] **zoro/models/backbone.py:39** - Need to investigate checkpoint_sequential compatibility
- [ ] **zoro/models/backbone.py:45** - Checkpoint compatibility issues between versions
- [ ] **zoro/models/head.py:11** - Output tensor shape mismatch for batch_size > 32
- [ ] **zoro/models/head.py:12** - Need to handle dynamic batch sizes properly
- [ ] **zoro/models/head.py:29** - Softmax numerical instability for large logits
- [ ] **zoro/models/head.py:30** - Consider using log_softmax for better numerical stability
- [ ] **zoro/utils/data_loader.py:7** - Memory not released after dataloader iteration
- [ ] **zoro/utils/data_loader.py:8** - Need to implement proper cleanup in __del__ method
- [ ] **zoro/utils/data_loader.py:18** - Prefetch queue grows unbounded
- [ ] **zoro/utils/data_loader.py:19** - Implement bounded queue with proper backpressure
- [ ] **zoro/utils/data_loader.py:41** - Worker processes not properly terminated
- [ ] **zoro/utils/data_loader.py:42** - Need to implement proper cleanup hooks
- [ ] **zoro/utils/transforms.py:6** - Image normalization values hardcoded
- [ ] **zoro/utils/transforms.py:7** - Should make these configurable or load from config file
- [ ] **zoro/utils/transforms.py:41** - Augmentation pipeline not deterministic with seed
- [ ] **zoro/utils/transforms.py:42** - Random state not properly saved and restored

## 🤝 Contributing

1. Pick a FIXME item from the issues list above
2. Fix the issue and add tests
3. Update this README when issues are resolved
