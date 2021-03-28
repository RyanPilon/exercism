from typing import List


def slices(series: str, length: int) -> List[str]:
    if length <= 0:
        raise ValueError("Length must be positive.")
    if length > len(series):
        raise ValueError("Length is longer than the length of the series.")

    start_indices = range(0, len(series) - length + 1)
    return [series[start : start + length] for start in start_indices]
