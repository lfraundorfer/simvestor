# Minimal in-memory store keyed by Flask session id
from typing import Dict, Any
store: Dict[str, Dict[str, Any]] = {}
