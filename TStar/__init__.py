"""
T*: Efficient Visual Search Framework for Long Videos

Installation:
    conda install -c conda-forge av
    pip install -e .

Usage:
    >>> from tstar import TStarFramework, TStarUniversalGrounder, initialize_heuristic
    >>> grounder = TStarUniversalGrounder(model_name='qwen')
    >>> heuristic = initialize_heuristic('owl-vit')
    >>> searcher = TStarFramework(video_path='video.mp4', question='...', ...)
"""

__version__ = "0.1.0"

# Direct imports (all the main classes users need)
from .TStarFramework import TStarFramework, initialize_heuristic
from .interface_grounding import TStarUniversalGrounder
from .interface_heuristic import HeuristicInterface

__all__ = [
    "TStarFramework",
    "TStarUniversalGrounder",
    "initialize_heuristic",
    "HeuristicInterface",
]