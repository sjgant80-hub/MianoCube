"""Layer 4: ISA-101 — HMI Design Standard.

Principle: Situational awareness > aesthetics.
5 layers of progressive detail.
Color = meaning, not decoration.

Tutorial:
    color = HMI_COLORS["alarm"]
    layer = HMI_LAYERS[0]  # Overview
"""

from dataclasses import dataclass

HMI_COLORS = {
    "normal":     {"hex": "#808080", "usage": "default, no action"},
    "running":    {"hex": "#00AA00", "usage": "active, operating"},
    "stopped":    {"hex": "#404040", "usage": "inactive, standby"},
    "warning":    {"hex": "#FFCC00", "usage": "attention needed"},
    "alarm":      {"hex": "#CC0000", "usage": "action required"},
    "maintenance":{"hex": "#0066CC", "usage": "out of service"},
    "manual":     {"hex": "#FF6600", "usage": "manual mode"},
    "transition": {"hex": "#00CCCC", "usage": "state changing"},
}


@dataclass
class HMILayer:
    level: int
    name: str
    scope: str
    info: str


HMI_LAYERS = [
    HMILayer(1, "Overview", "Plant/Site", "KPIs, Status, Alarms"),
    HMILayer(2, "Area", "Process Area", "Flows, States, Trends"),
    HMILayer(3, "Unit", "Equipment", "Faceplate, Control"),
    HMILayer(4, "Detail", "Diagnostic", "Config, Tuning"),
    HMILayer(5, "Support", "Maintenance", "Calibration, History"),
]

HMI_RULES = [
    "No hardcoded values in graphics",
    "Bind to tag path, not direct address",
    "Template→instance inheritance",
    "Centralized style definitions",
    "Alarm indication visible at all layers",
    "Navigation consistent, predictable",
    "Controls labeled, units shown",
    "Confirmation for critical commands",
]
