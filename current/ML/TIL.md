# 2025/05/31

**training**
- models learn patterns
- very high computational cost
- large batches
- forward and backwards pass (for gradient updates)
- goal of minimizing loss function and improving accuracy
- trained at large data centers and cloud providers

**inference**
- models predict
- lower computational cost (but high with millions of uses)
- forwards pass only

**hyperparameters**
configuration variables for a model
can tune these, ideally with bayesian optimization

---

what you get after training is a .pkl file for scikit-learn, .pb file for tensorflow, or .pt file for PyTorch