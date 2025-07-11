"""
Bioelectric Coherence Index (BCI) Calculator
Core implementation of the BCI formula for mental health assessment
"""

import numpy as np
from typing import Union, List

class BCICalculator:
    """
    Bioelectric Coherence Index Calculator
    Implements: BCI(t) = α·Φ(t) + β·Δ(t) - γ·Ψ(t)
    """
    
    def __init__(self, alpha: float = 1.0, beta: float = 0.8, gamma: float = 0.6):
        """Initialize BCI calculator with optimized parameters"""
        self.alpha = alpha  # Phase alignment weight
        self.beta = beta    # Circadian amplitude weight
        self.gamma = gamma  # Temporal variability weight
    
    def calculate_phase_alignment(self, light_timing: float, optimal_timing: float) -> float:
        """Calculate phase alignment component Φ(t)"""
        alignment = 1 - abs(light_timing - optimal_timing) / 12
        return max(0, min(1, alignment))
    
    def calculate_circadian_amplitude(self, light_exposure: List[float]) -> float:
        """Calculate circadian amplitude component Δ(t)"""
        if len(light_exposure) < 2:
            return 0.0
        
        amplitude = (max(light_exposure) - min(light_exposure)) / 10000
        return max(0, min(1, amplitude))
    
    def calculate_temporal_variability(self, sleep_times: List[float]) -> float:
        """Calculate temporal variability component Ψ(t)"""
        if len(sleep_times) < 2:
            return 0.0
        
        variability = np.std(sleep_times) / 6
        return max(0, min(1, variability))
    
    def calculate_bci(self, phase_alignment: float, amplitude: float, variability: float) -> float:
        """Calculate BCI score using core formula"""
        bci_score = (self.alpha * phase_alignment + 
                    self.beta * amplitude - 
                    self.gamma * variability) * 100
        
        return max(0, min(100, bci_score))
    
    def assess_condition_tier(self, bci_score: float) -> str:
        """Assess condition tier based on BCI score"""
        if bci_score >= 80:
            return "Core Circadian"
        elif bci_score >= 65:
            return "High Circadian"
        elif bci_score >= 50:
            return "Moderate Circadian"
        else:
            return "Lower Circadian"
