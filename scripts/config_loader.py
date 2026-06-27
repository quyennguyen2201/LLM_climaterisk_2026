"""Load project config from config.yaml, resolving {base_dir} placeholders."""
import os
import yaml
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent  # scripts/ -> repo root


def load_config(config_path=None):
    if config_path is None:
        config_path = _REPO_ROOT / "config.yaml"

    with open(config_path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    base = cfg["paths"]["base_dir"]
    cfg["paths"] = {
        k: v.replace("{base_dir}", base) if isinstance(v, str) else v
        for k, v in cfg["paths"].items()
    }

    for key in ("fig_folder", "rag_results_dir", "benchmark_output_dir", "tables_dir"):
        os.makedirs(cfg["paths"][key], exist_ok=True)

    return cfg
